"""
src/penalties_sla.py

Műszaki tartalom, szolgáltatási szintek és a kötbérrendszerek összehasonlító modellje.

Primer források:
- ÁSZ 1118. számú jelentés (43. és 51. oldal): Történelmi kötbér- és hiányossági képlet (K_h, K_f).
- MAÚT szakmai irányelvek és a 2022-es koncessziós szerződés 3/D. melléklete:
  Lézeres állapotfelmérés küszöbértékei (IRI, Nyomvályú, SFC).
"""

from typing import Dict, Any
import pandas as pd


def calculate_asz_historical_deduction(
    base_fee_m_huf: float = 267.6,
    phase_factor_kf: float = 1.0,
    deficiency_factor_kh: float = 0.985,  # Pl. 1.5% hiányossági levonás
    other_deductions_m_huf: float = 1.2    # Sebességkorlátozás miatti levonás
) -> Dict[str, float]:
    """
    Kiszámítja az ÁSZ 1118. jelentés szerinti tényleges RÁD-ot:
    RAD_tenyleges = RAD_bazis * Kf * Kh - D_egyeb
    """
    adjusted_fee = (base_fee_m_huf * phase_factor_kf * deficiency_factor_kh) - other_deductions_m_huf
    total_deduction = base_fee_m_huf - adjusted_fee
    return {
        "base_fee": base_fee_m_huf,
        "phase_factor_kf": phase_factor_kf,
        "deficiency_factor_kh": deficiency_factor_kh,
        "other_deductions": other_deductions_m_huf,
        "actual_fee": round(adjusted_fee, 2),
        "total_deduction": round(total_deduction, 2),
        "deduction_pct": round((total_deduction / base_fee_m_huf) * 100.0, 2)
    }


def evaluate_modern_sla(
    measured_iri: float,
    measured_rut_depth_mm: float,
    measured_sfc: float,
    iri_threshold: float = 1.8,
    rut_depth_threshold: float = 8.0,
    sfc_threshold: float = 0.45
) -> Dict[str, Any]:
    """
    Kiértékeli a modern lézeres állapotfelmérés eredményeit a szerződéses határértékekhez képest:
    - IRI <= 1.8 mm/m
    - Nyomvályúmélység <= 8.0 mm
    - SFC (tapadási tényező) >= 0.45
    """
    iri_pass = measured_iri <= iri_threshold
    rut_pass = measured_rut_depth_mm <= rut_depth_threshold
    sfc_pass = measured_sfc >= sfc_threshold
    all_pass = iri_pass and rut_pass and sfc_pass

    return {
        "iri": {"measured": measured_iri, "threshold": iri_threshold, "pass": iri_pass},
        "rut_depth": {"measured": measured_rut_depth_mm, "threshold": rut_depth_threshold, "pass": rut_pass},
        "sfc": {"measured": measured_sfc, "threshold": sfc_threshold, "pass": sfc_pass},
        "compliant": all_pass,
        "penalty_triggered": not all_pass
    }


def get_sla_comparison_table() -> pd.DataFrame:
    """Összeállítja a szankciórendszerek összehasonlító táblázatát."""
    rows = [
        {
            "Dimenzió / Modell": "2010 előtti PPP (ÁSZ 1118)",
            "Kötbér- és levonási mechanizmus": "RAD_tenyleges = RAD_bazis * Kf * Kh - D_egyeb",
            "Mérési módszertan": "Időszakos szakértői és hatósági állapotfelmérés, manuális hibajegyzőkönyvek",
            "Tényleges érvényesítés": "Az ÁSZ által ellenőrzött 10 hónapból 6-ban tényleges levonás történt",
            "Fő fókusz": "Üzemeltetési és burkolathibák, forgalomkorlátozások pénzügyi szankcionálása"
        },
        {
            "Dimenzió / Modell": "2022-es Koncesszió (MKIF)",
            "Kötbér- és levonási mechanizmus": "Szerződéses 3/D. melléklet: IRI <= 1.8 mm/m, Nyomvályú <= 8.0 mm, SFC >= 0.45",
            "Mérési módszertan": "Folyamatosan mozgó lézeres mérőautók, digitális felületdiagnosztika, WIM súlymérés",
            "Tényleges érvényesítés": "Automatizált küszöbérték-túllépési kötbér és levonási pontrendszer",
            "Fő fókusz": "Életciklus-szolgáltatási szintek, intelligens ITS és e-mobilitási (AFIR) infrastruktúra"
        }
    ]
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("=== SZOLGÁLTATÁSI SZINTEK ÉS KÖTBÉRRENDSZEREK ÖSSZEVETÉSE ===")
    df = get_sla_comparison_table()
    print(df.to_string(index=False))
