"""
src/km_tariff_comparison.py

A fajlagos kilométerdíjak reálérték- és árfolyam-korrekciós összehasonlító modellje.
Összeveti a 2010 előtti M6 PPP rendelkezésre állási díját a 2022-es MKIF koncesszió
indikatív kilométerdíjával.

Primer források:
- ÁSZ 1118. számú jelentés (43. és 51. oldal): M6 havi 22,3 M Ft/km/hó alapdíj, devizakockázat.
- KSH STADAT 1.1.1.31 és 1.1.1.32 termelői árindexek.
- G7 (2022. május) és Telex (2022. június) költségvetési feltáró elemzések (525 M Ft/km/év átlag).
"""

from typing import Dict, Any
import pandas as pd
try:
    from .ksh_chains import load_construction_annual, load_roads_subsector, calculate_chain_multiplier
except ImportError:
    from ksh_chains import load_construction_annual, load_roads_subsector, calculate_chain_multiplier


def calculate_m6_base_annual(monthly_fee_m_huf: float = 22.3) -> float:
    """Kiszámítja az M6 éves nominális bázisdíját (M Ft/km/év)."""
    return monthly_fee_m_huf * 12.0  # 267.6 M Ft/km/év


def method1_domestic_construction(
    base_annual_m_huf: float = 267.6,
    multiplier_melyepites: float = 2.348,
    multiplier_utak: float = 2.438
) -> Dict[str, float]:
    """
    1. Módszer: Belföldi építőipari termelői árindexálás (KSH).
    Visszaadja a mai reálértékű fajlagos díjat mélyépítésre és kifejezetten utakra.
    """
    fee_mely = base_annual_m_huf * multiplier_melyepites
    fee_utak = base_annual_m_huf * multiplier_utak
    return {
        "melyepites_multiplier": multiplier_melyepites,
        "melyepites_fee_m_huf": round(fee_mely, 1),
        "utak_multiplier": multiplier_utak,
        "utak_fee_m_huf": round(fee_utak, 1),
    }


def method2_contractual_fx(
    base_annual_m_huf: float = 267.6,
    fx_2010: float = 275.4,
    eu_inflation_factor: float = 1.45,
    fx_current: float = 395.0
) -> Dict[str, float]:
    """
    2. Módszer: Szerződéses euróalap és devizaárfolyam-korrekció.
    - 2010-es díj EUR-ban
    - Uniós mélyépítési infláció
    - Mai EUR/HUF árfolyam visszaváltás
    """
    fee_2010_eur = (base_annual_m_huf * 1_000_000.0) / fx_2010
    fee_current_huf = fee_2010_eur * eu_inflation_factor * fx_current
    fee_current_m_huf = fee_current_huf / 1_000_000.0
    return {
        "fx_2010": fx_2010,
        "fee_2010_eur": round(fee_2010_eur, 0),
        "eu_inflation_factor": eu_inflation_factor,
        "fx_current": fx_current,
        "fee_current_m_huf": round(fee_current_m_huf, 1),
    }


def calculate_relative_deltas(
    mkif_indicative_fee: float = 525.0,
    m6_melyepites: float = 628.3,
    m6_utak: float = 652.4,
    m6_eur: float = 556.5
) -> Dict[str, float]:
    """
    Kiszámítja az MKIF indikatív díjának relatív eltérését az M6 reálértékeihez képest:
    Delta = (MKIF - M6) / M6
    """
    delta_mely = (mkif_indicative_fee - m6_melyepites) / m6_melyepites
    delta_utak = (mkif_indicative_fee - m6_utak) / m6_utak
    delta_eur = (mkif_indicative_fee - m6_eur) / m6_eur
    return {
        "delta_melyepites_pct": round(delta_mely * 100.0, 1),
        "delta_utak_pct": round(delta_utak * 100.0, 1),
        "delta_eur_pct": round(delta_eur * 100.0, 1),
    }


def get_full_tariff_comparison_table() -> pd.DataFrame:
    """Összeállítja a tanulmány 2.2. fejezetének teljes összehasonlító táblázatát."""
    base_m6 = calculate_m6_base_annual(22.3)
    m1 = method1_domestic_construction(base_m6)
    m2 = method2_contractual_fx(base_m6)
    mkif_fee = 525.0
    deltas = calculate_relative_deltas(
        mkif_indicative_fee=mkif_fee,
        m6_melyepites=m1["melyepites_fee_m_huf"],
        m6_utak=m1["utak_fee_m_huf"],
        m6_eur=m2["fee_current_m_huf"]
    )

    rows = [
        {
            "Konstrukció / Módszer": "M6 PPP Bázis (2010, ÁSZ 1118)",
            "Fajlagos Díj (M Ft/km/év)": f"{base_m6:.1f}",
            "Indexálás / Árfolyam": "Nominális 2010-es bázis",
            "Relatív eltérés az MKIF-hez képest": "—"
        },
        {
            "Konstrukció / Módszer": "M6 Reálérték: KSH Mélyépítés (1.1.1.31)",
            "Fajlagos Díj (M Ft/km/év)": f"{m1['melyepites_fee_m_huf']:.1f}",
            "Indexálás / Árfolyam": f"KSH láncszorzó: {m1['melyepites_multiplier']:.3f} (+134.8%)",
            "Relatív eltérés az MKIF-hez képest": f"{deltas['delta_melyepites_pct']}%"
        },
        {
            "Konstrukció / Módszer": "M6 Reálérték: KSH Utak alcsoport (1.1.1.32)",
            "Fajlagos Díj (M Ft/km/év)": f"{m1['utak_fee_m_huf']:.1f}",
            "Indexálás / Árfolyam": f"KSH láncszorzó: {m1['utak_multiplier']:.3f} (+143.8%)",
            "Relatív eltérés az MKIF-hez képest": f"{deltas['delta_utak_pct']}%"
        },
        {
            "Konstrukció / Módszer": "M6 Reálérték: EUR deviza + EU infláció",
            "Fajlagos Díj (M Ft/km/év)": f"{m2['fee_current_m_huf']:.1f}",
            "Indexálás / Árfolyam": f"971 700 EUR * 1.45 * 395 Ft/EUR",
            "Relatív eltérés az MKIF-hez képest": f"{deltas['delta_eur_pct']}%"
        },
        {
            "Konstrukció / Módszer": "MKIF Koncesszió Indikatív Átlag (2022)",
            "Fajlagos Díj (M Ft/km/év)": f"{mkif_fee:.1f}",
            "Indexálás / Árfolyam": "Éves költségvetési keretből visszaszámított",
            "Relatív eltérés az MKIF-hez képest": "BÁZIS (0.0%)"
        }
    ]
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("=== FAJLAGOS KILOMÉTERDÍJAK ÖSSZEHASONLÍTÁSA (M6 vs MKIF) ===")
    df = get_full_tariff_comparison_table()
    print(df.to_string(index=False))
