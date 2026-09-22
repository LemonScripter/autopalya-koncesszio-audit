"""
src/engineering_m1.py

Indikatív mérnöki és logisztikai költségmodell az M1 autópálya forgalom alatti
2x3 sávos kapacitásbővítésére és a zöldmezős referencia-beruházásokra.

Primer források és mérnöki benchmarkok:
- MAÚT szakmai irányelvek és hazai gyorsforgalmi közbeszerzési szerződések.
- M1 M0 autóút és Győr közötti mintegy 78 km-es szakasz.
- All-in beruházási keretösszeg: 620 – 800 milliárd Ft.
"""

from typing import Dict, Any
import pandas as pd


def calculate_m1_widening_unit_costs(
    length_km: float = 78.0,
    min_budget_mrd: float = 620.0,
    max_budget_mrd: float = 800.0,
    direct_roadbed_min: float = 4.0,
    direct_roadbed_max: float = 5.5
) -> Dict[str, Any]:
    """
    Kiszámítja az M1 kapacitásbővítés közvetlen és all-in fajlagos költségeit.
    """
    all_in_min = min_budget_mrd / length_km
    all_in_max = max_budget_mrd / length_km
    return {
        "length_km": length_km,
        "direct_roadbed_min_mrd_per_km": direct_roadbed_min,
        "direct_roadbed_max_mrd_per_km": direct_roadbed_max,
        "total_budget_min_mrd": min_budget_mrd,
        "total_budget_max_mrd": max_budget_mrd,
        "all_in_min_mrd_per_km": round(all_in_min, 1),
        "all_in_max_mrd_per_km": round(all_in_max, 1),
    }


def get_engineering_benchmark_table() -> pd.DataFrame:
    """
    Generálja a tanulmány 3.1. fejezetében szereplő mérnöki költség-összehasonlító táblát.
    """
    m1_calc = calculate_m1_widening_unit_costs()
    rows = [
        {
            "Mérnöki kategória / Típus": "M1 Közvetlen pályaszerkezeti és alépítményi bővítés",
            "Műszaki tartalom": "Pályatest szélesítése (2x3 sáv + leállósáv), új kopó- és kötőrétegek, földművek",
            "Fajlagos költség (Mrd Ft / km)": f"{m1_calc['direct_roadbed_min_mrd_per_km']:.1f} – {m1_calc['direct_roadbed_max_mrd_per_km']:.1f}",
            "Definíciós megjegyzés": "Közvetlen kivitelezési ráfordítás"
        },
        {
            "Mérnöki kategória / Típus": "M1 Teljes projektköltségű mérnöki referencia (All-in)",
            "Műszaki tartalom": f"78 km-es M0–Győr szakasz, hidak/felüljárók újjáépítése, csomópontok, ITS, terelés ({int(m1_calc['total_budget_min_mrd'])}–{int(m1_calc['total_budget_max_mrd'])} Mrd Ft)",
            "Fajlagos költség (Mrd Ft / km)": f"{m1_calc['all_in_min_mrd_per_km']:.1f} – {m1_calc['all_in_max_mrd_per_km']:.1f}",
            "Definíciós megjegyzés": "Teljes beruházási program (folyó áron)"
        },
        {
            "Mérnöki kategória / Típus": "Zöldmezős referencia: Síkvidéki 2x2 sáv (pl. M44, M4)",
            "Műszaki tartalom": "Új nyomvonal kialakítása kedvező domborzati viszonyok között, rutin műtárgyakkal",
            "Fajlagos költség (Mrd Ft / km)": "3.8 – 4.8",
            "Definíciós megjegyzés": "Új építés (nem forgalom alatt)"
        },
        {
            "Mérnöki kategória / Típus": "Zöldmezős referencia: Hegyvidéki / műtárgyigényes (pl. M30)",
            "Műszaki tartalom": "Nehéz terepviszonyok, jelentős földmunkák, völgyhidak és komplex mérnöki műtárgyak",
            "Fajlagos költség (Mrd Ft / km)": "5.2 – 5.8",
            "Definíciós megjegyzés": "Új építés komplex geotechnikával"
        }
    ]
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("=== M1 KAPACITÁSBŐVÍTÉS ÉS ZÖLDMEZŐS MÉRNÖKI KÖLTSÉGMODELL ===")
    df = get_engineering_benchmark_table()
    print(df[["Mérnöki kategória / Típus", "Fajlagos költség (Mrd Ft / km)", "Definíciós megjegyzés"]].to_string(index=False))
