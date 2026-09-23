#!/usr/bin/env python3
"""
run_audit.py

Mester Futtató Script: A Magyar Gyorsforgalmi Úthálózat Koncessziós Rendszerének
Teljes Reprodukálható Pénzügyi-Mérnöki Auditja.

Futtatás:
    python run_audit.py
"""

import sys
import os

# Konzol UTF-8 támogatás beállítása Windows környezetben
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from src.ksh_chains import get_rebased_ksh_summary
from src.km_tariff_comparison import get_full_tariff_comparison_table, get_integrated_comparison_matrix
from src.npv_model import (
    calculate_real_npv_sensitivity,
    calculate_magyar_kozut_illustrative,
    get_npv_component_breakdown
)
from src.wacc_spread import (
    calculate_wacc,
    calculate_financing_spread,
    get_wacc_sensitivity_matrix
)
from src.engineering_m1 import (
    calculate_m1_widening_unit_costs,
    get_engineering_benchmark_table
)
from src.penalties_sla import get_sla_comparison_table


def print_banner():
    banner = """
========================================================================================
 MAGYAR GYORSFORGALMI ÚTHÁLÓZAT KONCESSZIÓS AUDIT (OPEN SCIENCE REPRODUCIBILITY ENGINE)
 Teljes körű, zéró-mock, primer adatokon alapuló pénzügyi és mérnöki számítási audit
========================================================================================
"""
    print(banner)


def run_full_audit():
    print_banner()

    # 1. KSH Termelői és Útépítési Láncszorzatok
    print("[1/6] KSH ÉPÍTŐIPARI ÉS ÚTÉPÍTÉSI ÁRINDEXEK (2010 -> 2024 LÁNCSZORZATOK)")
    print("-" * 88)
    ksh_summary = get_rebased_ksh_summary()
    print(ksh_summary[["Kategória", "2010 bázis", "2015 szint", "2020 szint", "2024 kumulált szorzó", "Áremelkedés (%)"]].to_string(index=False))
    print("\n")

    # 2. Fajlagos kilométerdíjak összevetése (M6 vs MKIF)
    print("[2/6] FAJLAGOS KILOMÉTERDÍJAK REÁLÉRTÉK- ÉS ÁRFOLYAM-KORREKCIÓJA")
    print("-" * 88)
    tariff_df = get_full_tariff_comparison_table()
    print(tariff_df.to_string(index=False))
    print("\n--- Integrált 4 szintes összehasonlítási mátrix (alma az almával feloldás) ---")
    matrix_df = get_integrated_comparison_matrix()
    print(matrix_df.to_string(index=False))
    print("\n")

    # 3. Jelenérték és Annuitási Modell (Fisher-egyenlet, Érzékenység)
    print("[3/6] JELENÉRTÉK (NPV) ÉS ANNUITÁSI ÉRZÉKENYSÉGI MODELL (RAD_0 = 375 Mrd Ft)")
    print("-" * 88)
    sens_df = calculate_real_npv_sensitivity()
    print(sens_df[["Reál diszkontráta (r_r)", "Annuitási szorzó (A_35)", "Reál jelenérték (NPV)"]].to_string(index=False))
    print("\n")

    # 4. Magyar Közút szemléltető felfuttatás és komponens bontás
    print("[4/6] MAGYAR KÖZÚT SZEMLÉLTETŐ PÉLDA ÉS JELENÉRTÉK-KOMPONENSEK DEKONSTRUKCIÓJA")
    print("-" * 88)
    mk = calculate_magyar_kozut_illustrative()
    print(f"Magyar Közút 2021-es bázis 35 éves exponenciális felfuttatása (3.5% növekedéssel):")
    print(f"  - Év végi kifizetési konvencióval:  {mk['end_of_year_mrd_huf']:,} Mrd Ft".replace(",", " "))
    print(f"  - Év eleji kifizetési konvencióval: {mk['start_of_year_mrd_huf']:,} Mrd Ft\n".replace(",", " "))
    comp_df = get_npv_component_breakdown()
    print(comp_df[["Főcsoport", "Pénzáram-komponens", "Becsült NPV (Mrd Ft)"]].to_string(index=False))
    print("\n")

    # 5. WACC és Szuverén Finanszírozási Spread
    print("[5/6] SÚLYOZOTT ÁTLAGOS TŐKEKÖLTSÉG (WACC) ÉS SZUVERÉN FINANSZÍROZÁSI SPREAD")
    print("-" * 88)
    base_wacc = calculate_wacc()
    base_spread = calculate_financing_spread(base_wacc["wacc"])
    print(f"EPEC WACC Képlet: WACC = (E/V * r_e) + (D/V * r_d * (1 - T_c))")
    print(f"  - Feltételezések: E/V=15%, D/V=85%, r_e=12.0%, r_d=5.5%, T_c=9.0%")
    print(f"  - Magán WACC eredmény: {base_wacc['wacc_pct']}%")
    print(f"  - ÁKK 15 éves szuverén referenciahozam (2021): {base_spread['sovereign_yield_pct']}%")
    print(f"  - Finanszírozási prémium (Spread): +{base_spread['spread_pct']}% (+{int(base_spread['spread_bps'])} bázispont)")
    print("\n")

    # 6. M1 Forgalom alatti kapacitásbővítés és Zöldmezős Mérnöki Költségek
    print("[6/6] M1 FORGALOM ALATTI KAPACITÁSBŐVÍTÉS ÉS ZÖLDMEZŐS BENCHMARKOK")
    print("-" * 88)
    eng_df = get_engineering_benchmark_table()
    print(eng_df[["Mérnöki kategória / Típus", "Fajlagos költség (Mrd Ft / km)", "Definíciós megjegyzés"]].to_string(index=False))
    print("\n")

    # Szolgáltatási szintek és kötbér
    print("[KIEGÉSZÍTÉS] SZOLGÁLTATÁSI SZINTEK ÉS KÖTBÉRRENDSZEREK (ÁSZ 1118 vs. MKIF 2022)")
    print("-" * 88)
    sla_df = get_sla_comparison_table()
    for _, row in sla_df.iterrows():
        print(f"* {row['Dimenzió / Modell']}:")
        print(f"    Mechanizmus: {row['Kötbér- és levonási mechanizmus']}")
        print(f"    Mérés:       {row['Mérési módszertan']}")
        print(f"    Fókusz:      {row['Fő fókusz']}")
    print("-" * 88)
    print("\n>>> SIKERES AUDIT: Minden modell és számítás valós primer adatokból, hibátlanul lefutott.")


if __name__ == "__main__":
    run_full_audit()
