# Magyar Gyorsforgalmi Úthálózat Koncessziós Audit (Open Science Repozitórium)

Ez a repozitórium tartalmazza a **„A magyar gyorsforgalmi úthálózat koncessziós rendszerének komplex elemzése”** című kutatás **teljes, 100%-ban reprodukálható számítási és adatbázis-architektúráját**.

A repozitórium célja, hogy bármely független kutató, elemző, újságíró vagy állampolgár saját gépén, külső függőségek és mock-adatok nélkül, gombnyomásra reprodukálhassa a tanulmányban közölt összes pénzügyi, statisztikai és mérnöki levezetést.

---

## Gyorsindítás (Quickstart)

### 1. Függőségek telepítése
```bash
pip install -r requirements.txt
```

### 2. Teljes audit futtatása parancssorból
```bash
python run_audit.py
```
A script valós primer adatokból kiindulva lefuttatja a KSH láncszorzatokat, az M6 vs. MKIF díjösszehasonlítást, a 35 éves jelenérték- és annuitásmodellt, a WACC-számítást és az M1 kapacitásbővítés mérnöki modelljét.

### 3. Szigorú matematikai és konzisztencia-tesztek (Pytest)
```bash
pytest tests/ -v
```
A tesztcsomag automatizált állításokkal (assertions) ellenőrzi, hogy a számítási eredmények tizedespontossággal megegyeznek-e a publikált tanulmány táblázataival.

### 4. Interaktív Jupyter Notebook
```bash
jupyter notebook notebooks/autopalya_koncesszio_audit.ipynb
```
Interaktív elemzés grafikonokkal, érzékenységi görbékkel és magyarázatokkal.

---

## Repozitórium Struktúra

```text
.
├── cikk/                                   # A publikált végleges tanulmány és összefoglaló fejezet
│   ├── A_magyar_gyorsforgalmi_uthalozat_koncesszios_rendszerenek_komplex_elemzese.md
│   └── vegleges_javasolt_osszefoglalas.md
├── data/                                   # Eredeti, primer dokumentumok és adatsorok
│   ├── 01_ASZ_Jelentesek/                  # ÁSZ 1118 (M6 PPP) és ÁSZ 1003 jelentések (PDF, TXT, MD)
│   ├── 02_Jogszabalyok/                    # Koncessziós tv., 1505/2021 Korm. hat., NKOI rendelet
│   ├── 03_KSH_Adatok/                      # Hivatalos KSH CPI és termelői árindex STADAT táblák (CSV)
│   ├── 04_Magyar_Kozut_Beszamolok/         # Magyar Közút 2020-2021 auditált éves beszámolók
│   ├── 05_Kuria_es_Birosagi_Iteletek/      # Kúria Pfv.IV.21.194/2023/15. ítélet és AB határozat
│   └── 06_Szakirodalom_Tokekoltseg/        # EPEC/EIB Value for Money, Voszka Éva, Major Iván tanulmányok
├── src/                                    # Pénzügyi-mérnöki audit forráskód (Zero-Mock)
│   ├── __init__.py
│   ├── ksh_chains.py                       # KSH árindexek beolvasása, láncszorzat-számítás, újrabázisolás
│   ├── km_tariff_comparison.py             # M6 PPP (2010) vs MKIF (2022) fajlagos díjmodell (KSH & EUR)
│   ├── npv_model.py                        # Fisher-diszkontálás, 35 éves annuitási mátrix, MK felfuttatás
│   ├── wacc_spread.py                      # EPEC WACC formula, tőkeszerkezet, szuverén finanszírozási spread
│   ├── engineering_m1.py                   # M1 2x3 sávos bővítés fajlagos költségmodellje vs zöldmezős referenciák
│   └── penalties_sla.py                    # ÁSZ 1118 hiányossági dedukció vs 2022 lézeres SLA küszöbök
├── tests/                                  # Automatizált reprodukálhatósági tesztcsomag
│   ├── __init__.py
│   └── test_reproducibility.py             # Pytest tesztek szigorú numerikus ellenőrzésekkel
├── notebooks/                              # Interaktív elemzői környezet
│   └── autopalya_koncesszio_audit.ipynb    # Jupyter Notebook vizualizációkkal és érzékenységi görbékkel
├── archive_dev_tools/                      # Eredeti kutatási scraperek, OCR scriptek és fejlesztői eszközök
├── pytest.ini                              # Pytest konfiguráció
├── requirements.txt                        # Python könyvtárfüggőségek
├── run_audit.py                            # Fő CLI futtató program
└── README.md                               # Repozitórium dokumentáció és master index
```

---

## Főbb Módszertani Összefüggések és Eredmények

### 1. KSH Építőipari és Útépítési Láncszorzatok ($2010 \to 2024$)
A 2010-es bázisdíjak reálértékre váltásához a KSH hivatalos éves láncindexeinek szorzatát képezzük:
$$I_{2010\to2024} = \prod_{t=2011}^{2024} \frac{\text{Index}_t}{100}$$
- **Mélyépítés (STADAT 1.1.1.31):** $2,348$ (+134,8% kumulált áremelkedés)
- **Utak alcsoport (STADAT 1.1.1.32):** $2,438$ (+143,8% kumulált áremelkedés)

### 2. Fajlagos Kilométerdíjak Összevetése
Az ÁSZ 1118. jelentés szerinti 2010-es havi 22,3 M Ft/km bázisdíj (évi **267,6 M Ft/km/év**) mai megfelelője:
- **1. Módszer (KSH Mélyépítés):** $267,6 \times 2,348 = \mathbf{628,3 \text{ M Ft/km/év}}$ ($\Delta_{\text{MKIF}} = -16,4\%$)
- **1. Módszer (KSH Utak):** $267,6 \times 2,438 = \mathbf{652,4 \text{ M Ft/km/év}}$ ($\Delta_{\text{MKIF}} = -19,5\%$)
- **2. Módszer (Szerződéses EUR + EU infláció):** $971\ 700 \text{ EUR} \times 1,45 \times 395 \text{ Ft/EUR} = \mathbf{556,5 \text{ M Ft/km/év}}$ ($\Delta_{\text{MKIF}} = -5,7\%$)
- **MKIF 2022 indikatív induló átlag:** $\mathbf{525,0 \text{ M Ft/km/év}}$ (a központi költségvetési keretből visszaszámított indikatív átlag az 1237 km-es hálózatra).

### 3. Jelenérték (NPV) és a Fisher-egyenlet
$$1 + r_n = (1 + r_r)(1 + \pi)$$
A 100%-ban CPI-indexált rendelkezésre állási díjak esetén a Fisher-összefüggés alapján az infláció semlegesítődik:
$$\text{PV} = \text{RÁD}_0 \times A_{35, r_r}, \quad A_{35, r_r} = \frac{1 - (1 + r_r)^{-35}}{r_r}$$
- $r_r = 3,5\%$ és $\text{RÁD}_0 = 375 \text{ Mrd Ft}$ esetén $A_{35} = 20,00 \implies \mathbf{7\ 500 \text{ Mrd Ft}}$ reál jelenérték.
- **Költségvetési szerződéses NPV összesen:** $\sim 10\ 600 – 12\ 100 \text{ Mrd Ft}$ (alapdíj + szintrehozási díj + M1 fejlesztési mérföldkövek).
- **Teljes közgazdasági erőforrás-ráfordítás:** $\sim 11\ 800 – 13\ 900 \text{ Mrd Ft}$ (magántőke finanszírozási prémiummal növelt érték).

### 4. Súlyozott Átlagos Tőkeköltség (WACC)
Az EPEC módszertan szerint:
$$WACC = \left( \frac{E}{V} \times r_e \right) + \left( \frac{D}{V} \times r_d \times (1 - T_c) \right)$$
$$WACC = (0,15 \times 0,12) + (0,85 \times 0,055 \times 0,91) = \mathbf{6,05\%}$$
- ÁKK 15 éves szuverén referenciahozam (2021): $r_g = 2,85\%$
- Finanszírozási különbözet (Spread): $\mathbf{+3,20\%}$ (+320 bázispont).

### 5. M1 Forgalom Alatti Kapacitásbővítés
- **Közvetlen pályaszerkezeti bővítés:** $4,0 – 5,5 \text{ Mrd Ft/km}$
- **All-in projektköltségű keret (78 km, 620–800 Mrd Ft):** $7,9 – 10,3 \text{ Mrd Ft/km}$ (hidak, felüljárók újjáépítésével, csomópontokkal, forgalomtereléssel).
- **Zöldmezős összehasonlító referenciák:** Síkvidéki: 3,8–4,8 Mrd Ft/km, hegyvidéki: 5,2–5,8 Mrd Ft/km.

---

## Elsődleges Hivatalos Források és Hivatkozások

1. **Állami Számvevőszék:** [1118. számú jelentés](file:///C:/Users/lszok/Documents/_autopalya/data/01_ASZ_Jelentesek/ASZ_1118.pdf) – Az M6/M60 PPP beruházások ellenőrzése.
2. **Központi Statisztikai Hivatal:** STADAT [1.1.1.2](file:///C:/Users/lszok/Documents/_autopalya/data/03_KSH_Adatok/KSH_Fogyasztoi_Arindexek_Eves.csv), [1.1.1.31](file:///C:/Users/lszok/Documents/_autopalya/data/03_KSH_Adatok/KSH_Epitoipar_Termeloi_Arindexek_Eves.csv), [1.1.1.32](file:///C:/Users/lszok/Documents/_autopalya/data/03_KSH_Adatok/KSH_Epitmenyfajtak_Termeloi_Arindexei.csv) táblák.
3. **Kúria:** [Pfv.IV.21.194/2023/15. felülvizsgálati ítélet](file:///C:/Users/lszok/Documents/_autopalya/data/05_Kuria_es_Birosagi_Iteletek/Kuria_Pfv_IV_21194_2023_15_Anonim_Itelet.pdf) – Koncessziós szerződésmellékletek közérdekű adatkiadása.
4. **Alkotmánybíróság:** [3372/2024. (X. 8.) AB végzés](file:///C:/Users/lszok/Documents/_autopalya/data/05_Kuria_es_Birosagi_Iteletek/3372_2024_AB_vegzes_MKIF_Autopalya.pdf) – Az MKIF alkotmányjogi panaszának visszautasítása.
5. **EPEC / Európai Beruházási Bank:** [The Guide to Guidance – Value for Money Assessment](file:///C:/Users/lszok/Documents/_autopalya/data/06_Szakirodalom_Tokekoltseg/EPEC_EIB_Value_for_Money_Assessment.pdf).

---
*Készült a tudományos nyitottság (Open Science) és az auditálhatóság szellemében.*
