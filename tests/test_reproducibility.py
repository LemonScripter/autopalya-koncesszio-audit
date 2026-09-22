"""
tests/test_reproducibility.py

Szigorú reprodukálhatósági és pénzügyi-matematikai tesztcsomag.
Ellenőrzi, hogy a tanulmányban publikált összes számítás, táblázat és képlet
valós adatokból, mock és dummy kód nélkül, 100%-os pontossággal előállítható-e.
"""

import os
import pytest
import math

from src.ksh_chains import (
    get_data_dir,
    load_cpi_annual,
    load_construction_annual,
    load_roads_subsector,
    calculate_chain_multiplier,
    get_rebased_ksh_summary
)
from src.km_tariff_comparison import (
    calculate_m6_base_annual,
    method1_domestic_construction,
    method2_contractual_fx,
    calculate_relative_deltas,
    get_full_tariff_comparison_table
)
from src.npv_model import (
    fisher_nominal_rate,
    annuity_factor,
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
from src.penalties_sla import (
    calculate_asz_historical_deduction,
    evaluate_modern_sla,
    get_sla_comparison_table
)


def test_data_integrity_no_mocks():
    """Ellenőrzi, hogy a primer adatok fizikailag léteznek a lemezen és nem üresek."""
    data_dir = get_data_dir()
    assert os.path.exists(data_dir), "A data könyvtár hiányzik!"
    
    files = [
        "KSH_Fogyasztoi_Arindexek_Eves.csv",
        "KSH_Epitoipar_Termeloi_Arindexek_Eves.csv",
        "KSH_Epitmenyfajtak_Termeloi_Arindexei.csv"
    ]
    for fn in files:
        fp = os.path.join(data_dir, fn)
        assert os.path.exists(fp), f"Hiányzó primer adatfájl: {fn}"
        assert os.path.getsize(fp) > 500, f"Gyanúsan kicsi vagy üres adatfájl: {fn}"


def test_ksh_chain_multipliers():
    """
    Ellenőrzi a KSH termelői árindexek 2010 -> 2024 láncszorzatát:
    - Utak alcsoport (1.1.1.32): 2.438 (+143.8%)
    - Mélyépítés (1.1.1.31): 2.348 (+134.8%)
    """
    roads = load_roads_subsector()
    utak_chain = calculate_chain_multiplier(roads, 2011, 2024)
    assert round(utak_chain, 3) == 2.438, f"Utak láncszorzat eltérés: {utak_chain}"
    
    constr = load_construction_annual()
    mely_raw = calculate_chain_multiplier(constr["melyepites"], 2011, 2024)
    assert round(mely_raw, 3) == 2.329, f"Mélyépítés nyers láncszorzat eltérés: {mely_raw}"
    
    summary_df = get_rebased_ksh_summary()
    assert len(summary_df) == 2
    assert "2.438" in summary_df.loc[1, "2024 kumulált szorzó"]
    assert "2.348" in summary_df.loc[0, "2024 kumulált szorzó"]


def test_m6_vs_mkif_tariffs():
    """
    Ellenőrzi a 2.2. fejezet fajlagos kilométerdíj-összehasonlítását:
    - M6 bázis: 22.3 * 12 = 267.6 M Ft/km/év
    - 1. Módszer (Mélyépítés, 2.348): 628.3 M Ft/km/év
    - 1. Módszer (Utak, 2.438): 652.4 M Ft/km/év
    - 2. Módszer (EUR deviza): 556.5 M Ft/km/év
    - Relatív különbségek az 525 M Ft MKIF díjhoz képest: -16.4%, -19.5%, -5.7%
    """
    base_m6 = calculate_m6_base_annual(22.3)
    assert base_m6 == 267.6

    m1 = method1_domestic_construction(base_m6, multiplier_melyepites=2.348, multiplier_utak=2.438)
    assert m1["melyepites_fee_m_huf"] == 628.3
    assert m1["utak_fee_m_huf"] == 652.4

    m2 = method2_contractual_fx(base_m6, fx_2010=275.4, eu_inflation_factor=1.45, fx_current=395.0)
    assert m2["fee_current_m_huf"] == 556.5

    deltas = calculate_relative_deltas(525.0, m1["melyepites_fee_m_huf"], m1["utak_fee_m_huf"], m2["fee_current_m_huf"])
    assert deltas["delta_melyepites_pct"] == -16.4
    assert deltas["delta_utak_pct"] == -19.5
    assert deltas["delta_eur_pct"] == -5.7


def test_npv_and_fisher_annuity():
    """
    Ellenőrzi a 2.1. fejezet jelenérték- és annuitásszámításait:
    - Fisher-képlet
    - Annuitási szorzók (A_35,rr): r_r=3.5% esetén 20.00
    - Reál jelenérték r_r=3.5% és RAD_0=375 Mrd mellett: 7500 Mrd Ft
    - Magyar Közút szemléltető 35 éves felfuttatása: ~26 640 Mrd Ft
    """
    # Fisher formula
    r_n = fisher_nominal_rate(real_rate=0.035, inflation=0.03)
    expected_rn = 0.035 + 0.03 + (0.035 * 0.03)
    assert abs(r_n - expected_rn) < 1e-9

    # Annuitás r_r = 3.5%
    a35_35 = annuity_factor(0.035, 35)
    assert round(a35_35, 2) == 20.00
    npv_35 = 375.0 * a35_35
    assert round(npv_35) == 7500

    # Annuitás r_r = 2.5%
    a35_25 = annuity_factor(0.025, 35)
    assert round(a35_25, 2) == 23.15
    npv_25 = 375.0 * a35_25
    assert round(npv_25) == 8679 or round(npv_25) == 8680

    # Magyar Közút szemléltető felfuttatás
    mk = calculate_magyar_kozut_illustrative(base_budget_2021_mrd=386.05, annual_rate=0.035, years=35)
    assert abs(mk["end_of_year_mrd_huf"] - 26640) < 5
    assert abs(mk["start_of_year_mrd_huf"] - 25740) < 5


def test_wacc_and_financing_spread():
    """
    Ellenőrzi a WACC-képletet és a szuverén finanszírozási spreadet (5.1. fejezet):
    - WACC = (0.15 * 0.12) + (0.85 * 0.055 * 0.91) = 6.05%
    - r_g = 2.85%
    - Spread = +3.20% (+320 bázispont)
    """
    res = calculate_wacc(
        equity_ratio=0.15,
        debt_ratio=0.85,
        cost_of_equity=0.12,
        cost_of_debt=0.055,
        tax_rate=0.09
    )
    assert res["wacc_pct"] == 6.05
    assert round(res["equity_component"], 3) == 0.018
    assert round(res["debt_component"], 4) == 0.0425

    spread = calculate_financing_spread(wacc=res["wacc"], sovereign_yield=0.0285)
    assert spread["spread_pct"] == 3.20
    assert spread["spread_bps"] == 320


def test_m1_engineering_widening():
    """
    Ellenőrzi az M1 forgalom alatti 2x3 sávos bővítés fajlagos költségmodelljét (3.1. fejezet):
    - Hossz: 78 km (M0 - Győr)
    - Teljes beruházási keret: 620 - 800 Mrd Ft
    - All-in fajlagos költség: 7.9 - 10.3 Mrd Ft / km
    - Közvetlen pályaszerkezet: 4.0 - 5.5 Mrd Ft / km
    """
    m1 = calculate_m1_widening_unit_costs(length_km=78.0, min_budget_mrd=620.0, max_budget_mrd=800.0)
    assert m1["all_in_min_mrd_per_km"] == 7.9
    assert m1["all_in_max_mrd_per_km"] == 10.3
    assert m1["direct_roadbed_min_mrd_per_km"] == 4.0
    assert m1["direct_roadbed_max_mrd_per_km"] == 5.5


def test_penalties_sla_modern_thresholds():
    """
    Ellenőrzi a szerződéses szolgáltatási szinteket és határértékeket (4.1. fejezet):
    - IRI <= 1.8 mm/m
    - Nyomvályú <= 8.0 mm
    - SFC >= 0.45
    """
    # Megfelelő pálya
    eval_pass = evaluate_modern_sla(measured_iri=1.5, measured_rut_depth_mm=6.2, measured_sfc=0.52)
    assert eval_pass["compliant"] is True
    assert eval_pass["penalty_triggered"] is False

    # Nem megfelelő pálya (IRI túllépés)
    eval_fail = evaluate_modern_sla(measured_iri=2.1, measured_rut_depth_mm=6.2, measured_sfc=0.52)
    assert eval_fail["compliant"] is False
    assert eval_fail["penalty_triggered"] is True
    assert eval_fail["iri"]["pass"] is False
