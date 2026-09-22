"""
src/wacc_spread.py

A súlyozott átlagos tőkeköltség (WACC) és a szuverén finanszírozási spread modellje.

Módszertani alap:
- EPEC / EIB: Value for Money Assessment Guide
- Képlet: WACC = (E/V * r_e) + (D/V * r_d * (1 - T_c))
- Szuverén referenciahozam (ÁKK 2021): r_g = 2.85%
"""

from typing import Dict, List, Tuple
import pandas as pd


def calculate_wacc(
    equity_ratio: float = 0.15,
    debt_ratio: float = 0.85,
    cost_of_equity: float = 0.12,
    cost_of_debt: float = 0.055,
    tax_rate: float = 0.09
) -> Dict[str, float]:
    """
    Kiszámítja a WACC-ot az EPEC képlete alapján.
    """
    assert abs((equity_ratio + debt_ratio) - 1.0) < 1e-6, "A tőkesúlyok összegének 1.0-nak kell lennie!"
    equity_comp = equity_ratio * cost_of_equity
    debt_comp = debt_ratio * cost_of_debt * (1.0 - tax_rate)
    wacc = equity_comp + debt_comp
    return {
        "equity_ratio": equity_ratio,
        "debt_ratio": debt_ratio,
        "cost_of_equity": cost_of_equity,
        "cost_of_debt": cost_of_debt,
        "tax_rate": tax_rate,
        "equity_component": equity_comp,
        "debt_component": debt_comp,
        "wacc": wacc,
        "wacc_pct": round(wacc * 100.0, 2)
    }


def calculate_financing_spread(
    wacc: float = 0.0605025,
    sovereign_yield: float = 0.0285
) -> Dict[str, float]:
    """
    Finanszírozási különbség (tőkeköltség-prémium) a magán-WACC és a szuverén kötvényhozam között.
    """
    spread = wacc - sovereign_yield
    return {
        "wacc_pct": round(wacc * 100.0, 2),
        "sovereign_yield_pct": round(sovereign_yield * 100.0, 2),
        "spread_pct": round(spread * 100.0, 2),
        "spread_bps": round(spread * 10_000.0, 0)
    }


def get_wacc_sensitivity_matrix(
    equity_ratio: float = 0.15,
    tax_rate: float = 0.09,
    re_values: List[float] = [0.10, 0.12, 0.14],
    rd_values: List[float] = [0.045, 0.055, 0.065],
    sovereign_yield: float = 0.0285
) -> pd.DataFrame:
    """
    Érzékenységi mátrix az elvárt saját tőke hozamra (r_e) és a banki hitelkamatra (r_d).
    """
    rows = []
    debt_ratio = 1.0 - equity_ratio
    for re in re_values:
        for rd in rd_values:
            res = calculate_wacc(equity_ratio, debt_ratio, re, rd, tax_rate)
            spread = calculate_financing_spread(res["wacc"], sovereign_yield)
            rows.append({
                "Saját tőke elvárt hozam (r_e)": f"{re*100:.1f}%",
                "Hitelkamatláb (r_d)": f"{rd*100:.1f}%",
                "WACC (%)": f"{res['wacc_pct']:.2f}%",
                "Szuverén hozam (r_g)": f"{sovereign_yield*100:.2f}%",
                "Finanszírozási Spread": f"+{spread['spread_pct']:.2f}% ({int(spread['spread_bps'])} bps)",
                "wacc_raw": res["wacc"],
                "spread_raw": res["wacc"] - sovereign_yield
            })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("=== SÚLYOZOTT ÁTLAGOS TŐKEKÖLTSÉG (WACC) ÉS FINANSZÍROZÁSI SPREAD ===")
    base_wacc = calculate_wacc()
    base_spread = calculate_financing_spread(base_wacc["wacc"])
    print(f"Magán WACC: {base_wacc['wacc_pct']}% (Saját tőke rész: {base_wacc['equity_component']*100:.2f}%, Hitel rész: {base_wacc['debt_component']*100:.2f}%)")
    print(f"ÁKK referenciahozam (2021): {base_spread['sovereign_yield_pct']}%")
    print(f"Finanszírozási prémium (Spread): +{base_spread['spread_pct']}% ({int(base_spread['spread_bps'])} bázispont)")

    print("\n=== WACC ÉS SPREAD ÉRZÉKENYSÉGI MÁTRIX ===")
    matrix = get_wacc_sensitivity_matrix()
    print(matrix[["Saját tőke elvárt hozam (r_e)", "Hitelkamatláb (r_d)", "WACC (%)", "Finanszírozási Spread"]].to_string(index=False))
