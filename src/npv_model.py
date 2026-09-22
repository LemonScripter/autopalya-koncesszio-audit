"""
src/npv_model.py

A 35 éves koncessziós modell jelenérték- (NPV), diszkontálási és érzékenységi számításai.

Főbb funkciók:
1. Fisher-összefüggés (nominális és reálkamat közötti kapcsolat)
2. 35 éves diszkrét idejű annuitási faktorok (A_35,rr)
3. Inflációtól semlegesített reálértékű NPV érzékenységi mátrix (1.5%, 2.5%, 3.5%, 4.5%)
4. Kumulált nominális kifizetés tényleges KSH inflációval és hosszú távú rátával
5. Magyar Közút szemléltető 35 éves exponenciális felfuttatása (26 640 Mrd Ft)
6. A jelenérték komponenseinek dekonstrukciója (költségvetési szerződéses NPV vs. közgazdasági modell)
"""

from typing import Dict, List, Tuple
import pandas as pd


def fisher_nominal_rate(real_rate: float, inflation: float) -> float:
    """
    Fisher-egyenlet: (1 + r_n) = (1 + r_r) * (1 + pi)
    r_n = r_r + pi + r_r * pi
    """
    return (1.0 + real_rate) * (1.0 + inflation) - 1.0


def annuity_factor(real_rate: float, years: int = 35) -> float:
    """
    A_T,r = (1 - (1 + r)^(-T)) / r
    """
    if real_rate == 0:
        return float(years)
    return (1.0 - (1.0 + real_rate) ** (-years)) / real_rate


def calculate_real_npv_sensitivity(
    rad0_mrd_huf: float = 375.0,
    real_rates: List[float] = [0.015, 0.025, 0.035, 0.045],
    inflation_scenarios: List[float] = [0.025, 0.035, 0.050]
) -> pd.DataFrame:
    """
    Generálja a tanulmány 2.1. fejezetében található reálértékű NPV érzékenységi táblázatot.
    A Fisher-elv alapján a 100%-ban indexált pénzáramok reál jelenértéke független az inflációtól.
    """
    rows = []
    for rr in real_rates:
        af = annuity_factor(rr, 35)
        npv = rad0_mrd_huf * af
        row = {
            "Reál diszkontráta (r_r)": f"{rr*100:.1f}%",
            "Várható infláció (pi=2.5%)": f"{round(npv):,} Mrd Ft".replace(",", " "),
            "Várható infláció (pi=3.5%)": f"{round(npv):,} Mrd Ft".replace(",", " "),
            "Várható infláció (pi=5.0%)": f"{round(npv):,} Mrd Ft".replace(",", " "),
            "Annuitási szorzó (A_35)": round(af, 2),
            "Reál jelenérték (NPV)": f"{round(npv):,} Mrd Ft".replace(",", " "),
            "npv_exact": npv,
            "annuity_exact": af
        }
        rows.append(row)
    return pd.DataFrame(rows)


def calculate_cumulative_nominal(
    rad0_net_base_mrd: float = 250.0,
    cpi_actual: List[float] = [0.145, 0.176, 0.037],
    cpi_longterm: float = 0.035,
    years: int = 35
) -> float:
    """
    Kiszámítja a 35 éves kumulált nominális kifizetést:
    sum_{t=1}^{35} [ RAD_0 * prod_{i=1}^t (1 + pi_i) ]
    """
    cpi_series = list(cpi_actual) + [cpi_longterm] * (years - len(cpi_actual))
    cum_total = 0.0
    compound_inflation = 1.0
    for t in range(years):
        compound_inflation *= (1.0 + cpi_series[t])
        cum_total += rad0_net_base_mrd * compound_inflation
    return cum_total


def calculate_magyar_kozut_illustrative(
    base_budget_2021_mrd: float = 386.0,
    annual_rate: float = 0.035,
    years: int = 35
) -> Dict[str, float]:
    """
    Magyar Közút szemléltető 35 éves exponenciális felfuttatása:
    Év végi kifizetési konvenció: 386 * 1.035 * (1.035^35 - 1) / 0.035 = ~26 640 Mrd Ft
    Év eleji konvenció: 386 * (1.035^35 - 1) / 0.035 = ~25 740 Mrd Ft
    """
    growth_sum_end = base_budget_2021_mrd * (1.0 + annual_rate) * ((1.0 + annual_rate) ** years - 1.0) / annual_rate
    growth_sum_start = base_budget_2021_mrd * ((1.0 + annual_rate) ** years - 1.0) / annual_rate
    return {
        "end_of_year_mrd_huf": round(growth_sum_end, 0),
        "start_of_year_mrd_huf": round(growth_sum_start, 0),
    }


def get_npv_component_breakdown() -> pd.DataFrame:
    """
    A 2.1. fejezet 3. pontjában szereplő strukturált jelenérték-dekonstrukció:
    Költségvetési szerződéses kifizetések vs. Magánfinanszírozási többletteher.
    """
    rows = [
        {
            "Főcsoport": "I. Költségvetési szerződéses kifizetések",
            "Pénzáram-komponens": "Alap RÁD",
            "Éves ráfordítás / Bázis": "~360 – 390 Mrd Ft / év",
            "Tartalom és mechanizmus": "Üzemeltetés és rutinfenntartás szerződéses alapdíja (CPI-követő)",
            "Időtáv": "35 év",
            "Becsült NPV (Mrd Ft)": "~7 200 – 7 800"
        },
        {
            "Főcsoport": "I. Költségvetési szerződéses kifizetések",
            "Pénzáram-komponens": "RÁASZD (Szintrehozási díj)",
            "Éves ráfordítás / Bázis": "~60 – 80 Mrd Ft / év",
            "Tartalom és mechanizmus": "538 km gyorsított felújításának tőketörlesztési díjeleme",
            "Időtáv": "1–11. év",
            "Becsült NPV (Mrd Ft)": "~600 – 800"
        },
        {
            "Főcsoport": "I. Költségvetési szerződéses kifizetések",
            "Pénzáram-komponens": "Fejlesztési díjak (M1 bővítés)",
            "Éves ráfordítás / Bázis": "Célzott mérföldkövek",
            "Tartalom és mechanizmus": "Forgalom alatti 2x3 sávos bővítés, hidak, csomópontok beruházási díjai",
            "Időtáv": "1–10. év",
            "Becsült NPV (Mrd Ft)": "~2 800 – 3 500"
        },
        {
            "Főcsoport": "I. KÖLTSÉGVETÉSI SZERZŐDÉSES NPV ÖSSZESEN",
            "Pénzáram-komponens": "Közvetlen állami kiadás jelenértéke",
            "Éves ráfordítás / Bázis": "—",
            "Tartalom és mechanizmus": "Szerződéses kifizetési kötelezettségek diszkontált összege (3.5% r_r)",
            "Időtáv": "35 év",
            "Becsült NPV (Mrd Ft)": "~10 600 – 12 100"
        },
        {
            "Főcsoport": "II. Finanszírozási és közgazdasági modell",
            "Pénzáram-komponens": "Finanszírozási modell többletköltsége",
            "Éves ráfordítás / Bázis": "Indikatív tőkeköltség-prémium",
            "Tartalom és mechanizmus": "Koncesszori tőkeáttételből, DSRA tartalékból és WACC-felárból származó közgazdasági többletteher",
            "Időtáv": "35 év",
            "Becsült NPV (Mrd Ft)": "~1 200 – 1 800"
        },
        {
            "Főcsoport": "TELJES KÖZGAZDASÁGI ERŐFORRÁS-RÁFORDÍTÁS",
            "Pénzáram-komponens": "Szerződéses NPV + Finanszírozási prémium",
            "Éves ráfordítás / Bázis": "—",
            "Tartalom és mechanizmus": "Társadalmi erőforrás-ráfordítás teljes közgazdasági értéke",
            "Időtáv": "35 év",
            "Becsült NPV (Mrd Ft)": "~11 800 – 13 900"
        }
    ]
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("=== 1. INFLÁCIÓTÓL SEMLEGESÍTETT REÁL JELENÉRTÉK ÉRZÉKENYSÉG ===")
    sens_df = calculate_real_npv_sensitivity()
    print(sens_df[["Reál diszkontráta (r_r)", "Annuitási szorzó (A_35)", "Reál jelenérték (NPV)"]].to_string(index=False))

    print("\n=== 2. MAGYAR KÖZÚT SZEMLÉLTETŐ 35 ÉVES FELFUTTATÁS ===")
    mk = calculate_magyar_kozut_illustrative()
    print(f"Év végi kifizetési konvencióval: {mk['end_of_year_mrd_huf']:,} Mrd Ft".replace(",", " "))
    print(f"Év eleji kifizetési konvencióval: {mk['start_of_year_mrd_huf']:,} Mrd Ft".replace(",", " "))

    print("\n=== 3. JELENÉRTÉK-KOMPONENSEK STRUKTURÁLT BONTÁSA ===")
    comp_df = get_npv_component_breakdown()
    print(comp_df[["Főcsoport", "Pénzáram-komponens", "Becsült NPV (Mrd Ft)"]].to_string(index=False))
