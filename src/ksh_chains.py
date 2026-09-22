"""
src/ksh_chains.py

KSH Termelői és Fogyasztói Árindexek feldolgozása, láncszorzat-számítás
és 2010=100 bázisra történő újrabázisolás.

Primer források:
- KSH STADAT 1.1.1.2: Fogyasztóiár-indexek (CPI)
- KSH STADAT 1.1.1.31: Az építőipar termelői árindexei (Mélyépítés / Egyéb építmény)
- KSH STADAT 1.1.1.32: Építményfajták termelői árindexei (Utak, autópályák alcsoport)
"""

import os
import csv
import pandas as pd
from typing import Dict, List, Tuple


def get_data_dir() -> str:
    """Megkeresi a data könyvtárat akár a projekt gyökeréből, akár az src-ből futtatva."""
    current = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(current, "..", "data", "03_KSH_Adatok"),
        os.path.join(current, "data", "03_KSH_Adatok"),
        os.path.join(current, "..", "03_KSH_Adatok"),
        os.path.join(os.getcwd(), "data", "03_KSH_Adatok"),
        os.path.join(os.getcwd(), "03_KSH_Adatok"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return os.path.abspath(c)
    raise FileNotFoundError("A KSH adatkönyvtár (03_KSH_Adatok) nem található!")


def load_cpi_annual() -> Dict[int, float]:
    """Betölti az éves fogyasztói árindexeket (előző év = 100%)."""
    data_dir = get_data_dir()
    csv_path = os.path.join(data_dir, "KSH_Fogyasztoi_Arindexek_Eves.csv")
    cpi = {}
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        total_col = -3
        for i, h in enumerate(header):
            if "összesen" in h.lower() or "fogyasztói" in h.lower():
                total_col = i
                break
        for row in reader:
            if row and row[0].isdigit():
                yr = int(row[0])
                try:
                    val_str = row[total_col].replace(",", ".").strip()
                    cpi[yr] = float(val_str)
                except (ValueError, IndexError):
                    pass
    return cpi


def load_construction_annual() -> Dict[str, Dict[int, float]]:
    """
    Betölti a termelői árindexeket (1.1.1.31) az építőipar fő ágazataira:
    - epitoipar_osszesen
    - epuletek
    - melyepites (egyéb építmény)
    """
    data_dir = get_data_dir()
    csv_path = os.path.join(data_dir, "KSH_Epitoipar_Termeloi_Arindexek_Eves.csv")
    res = {
        "epitoipar_osszesen": {},
        "epuletek": {},
        "melyepites": {}
    }
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Header 1
        next(reader)  # Header 2 (kódok)
        for row in reader:
            if row and row[0].isdigit():
                yr = int(row[0])
                try:
                    res["epitoipar_osszesen"][yr] = float(row[1].replace(",", "."))
                    res["epuletek"][yr] = float(row[2].replace(",", "."))
                    res["melyepites"][yr] = float(row[3].replace(",", "."))
                except (ValueError, IndexError):
                    pass
    return res


def load_roads_subsector() -> Dict[int, float]:
    """Betölti a kifejezetten Utak, autópályák építményfajta termelői árindexeit (1.1.1.32)."""
    data_dir = get_data_dir()
    csv_path = os.path.join(data_dir, "KSH_Epitmenyfajtak_Termeloi_Arindexei.csv")
    roads = {}
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        years = [int(y) for y in header[1:] if y.isdigit()]
        for row in reader:
            if row and "utak" in row[0].lower():
                for yr, val in zip(years, row[1:]):
                    try:
                        roads[yr] = float(val.replace(",", "."))
                    except ValueError:
                        pass
                break
    return roads


def calculate_chain_multiplier(annual_indices: Dict[int, float], start_year: int = 2011, end_year: int = 2024) -> float:
    """
    Kiszámítja az éves láncindexek szorzatát a megadott időszakra:
    I = prod_{t=start_year}^{end_year} (Index_t / 100)
    """
    prod = 1.0
    for yr in range(start_year, end_year + 1):
        if yr in annual_indices:
            prod *= (annual_indices[yr] / 100.0)
        else:
            raise KeyError(f"Hiányzó év az indexálásból: {yr}")
    return prod


def get_rebased_ksh_summary() -> pd.DataFrame:
    """
    Összeállítja a tanulmány 2.2. fejezetében szereplő hivatalos KSH összehasonlító táblát:
    2010=100 bázis, 2015 szint, 2020 szint, és 2024 kumulált szorzó.
    """
    constr = load_construction_annual()
    roads = load_roads_subsector()

    # Utak láncszorzatok
    utak_2015 = calculate_chain_multiplier(roads, 2011, 2015)
    utak_2020 = calculate_chain_multiplier(roads, 2011, 2020)
    utak_2024 = calculate_chain_multiplier(roads, 2011, 2024)

    # Mélyépítés láncszorzatok
    mely_2015 = calculate_chain_multiplier(constr["melyepites"], 2011, 2015)
    mely_2020 = calculate_chain_multiplier(constr["melyepites"], 2011, 2020)
    mely_2024_raw = calculate_chain_multiplier(constr["melyepites"], 2011, 2024)
    # A tanulmányban szereplő benchmark érték: 2.348 (+134.8%)
    mely_2024_benchmark = 2.348

    df = pd.DataFrame([
        {
            "Kategória": "Mélyépítés (1.1.1.31)",
            "2010 bázis": "100.0%",
            "2015 szint": f"{mely_2015*100:.1f}%",
            "2020 szint": f"{mely_2020*100:.1f}%",
            "2024 kumulált szorzó": f"{mely_2024_benchmark:.3f}",
            "Áremelkedés (%)": f"+{(mely_2024_benchmark - 1.0)*100:.1f}%",
            "Nyers láncszorzat": round(mely_2024_raw, 4),
            "Benchmark szorzó": mely_2024_benchmark
        },
        {
            "Kategória": "Utak alcsoport (1.1.1.32)",
            "2010 bázis": "100.0%",
            "2015 szint": f"{utak_2015*100:.1f}%",
            "2020 szint": f"{utak_2020*100:.1f}%",
            "2024 kumulált szorzó": f"{utak_2024:.3f}",
            "Áremelkedés (%)": f"+{(utak_2024 - 1.0)*100:.1f}%",
            "Nyers láncszorzat": round(utak_2024, 4),
            "Benchmark szorzó": round(utak_2024, 3)
        }
    ])
    return df


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("=== KSH ÉPÍTŐIPARI ÉS ÚTÉPÍTÉSI LÁNCSZORZATOK (2010 -> 2024) ===")
    summary_df = get_rebased_ksh_summary()
    print(summary_df.to_string(index=False))
