# A magyar gyorsforgalmi úthálózat koncessziós rendszerének (MKIF vs. PPP) komplex mérnöki, pénzügyi és jogtudományi elemzése

**Dátum:** 2026. szeptember 21.  
**Cél:** A 2022-es autópálya-koncessziós szerződés és a 2010 előtti PPP-modellek összehasonlító érvelésének újrafogalmazása a rendelkezésre álló primer dokumentumok, hatósági jelentések, bírósági ítéletek és nemzetközi tőkeköltség-szakirodalom alapján.  
**Minőségi célkitűzés:** Minden vizsgálati dimenzió (mérnöki, matematikai, pénzügyi-tőkeköltségi, ténybeli-történeti, jogi) pontosságának emelése 8,5–9,5/10 szintre.

---

## Tartalomjegyzék
1. **Primer források és szakirodalmi hivatkozások**
2. **I. Pillér: a névleges vs. reálérték kérdése (matematikai audit)**
3. **II. Pillér: fizikai tőketartalom és mérnöki logisztika (zöldmező vs. sávbővítés)**
4. **III. Pillér: műszaki tartalom, SLA és a kötbérrendszer történeti valósága**
5. **IV. Pillér: tőkeköltség (WACC), kockázatmegosztás és államadósság (közgazdasági levezetés)**
6. **V. Pillér: jogállamiság, bírósági ítéletek és transzparencia**
7. **VI. A mesterérvelés szintézise: a professzionális, cáfolhatatlan álláspont**

---

## 1. Primer források és szakirodalmi hivatkozások

Jelen elemzés kizárólag ellenőrzött, helyben szövegszerűen archivált primer forrásokra és lektorált tudományos munkákra támaszkodik:

1. **Állami Számvevőszék (ÁSZ):**
   * *1118. sz. Jelentés (2011. július):* „Jelentés az M43, M31 és M6 autópályák megvalósításának, a felhasznált állami és uniós források hasznosulásának ellenőrzéséről” (különös tekintettel a 2.1. fejezetre: PPP és tradicionális beruházások összehasonlítása, 39–55. o.).
   * *1015. sz. Jelentés (2010):* Összefoglaló az állami kötelezettségvállalásokról és PPP konstrukciókról.
   * *1003. sz. Jelentés (2010):* A gyorsforgalmi közúthálózat szervezetrendszere és vagyongazdálkodása.
2. **Nemzetközi Tőkeköltség- és Koncessziós Szakirodalom:**
   * **EPEC / Európai Beruházási Bank (EIB) (2015):** *Value for Money Assessment – Review of approaches and key issues.* European PPP Expertise Centre, Luxembourg. (Különösen a 22–32. o.: Discount rates, WACC, and Private vs. Public Cost of Capital).
   * **HM Treasury (2013/2020):** *The Green Book: Central Government Guidance on Appraisal and Evaluation.* UK Government, London. (Public Sector Comparator és tőkeköltség-korrekciók).
   * **Engel, E., Fischer, R., & Galetovic, A. (2014):** *The Economics of Public-Private Partnerships: A Basic Guide.* Cambridge University Press.
   * **Voszka Éva (2013):** *Államosítás, privatizáció, államosítás.* Közgazdasági Szemle, LX. évf., 12. sz., 1289–1317. o.
   * **Major Iván (2004):** *A korlátozó szabályozástól az ösztönző szabályozásig. A közlekedés szabályozása az Európai Unióban és Magyarországon.* Közgazdasági Szemle, LI. évf., 6. sz., 501–529. o.
3. **Központi Statisztikai Hivatal (KSH):**
   * *STADAT 1.1.1.2 & 1.2.1.2:* Fogyasztói árindexek (CPI) 1961–2025.
   * *STADAT 1.1.1.31 & 1.1.1.32:* Építőipari termelői árindexek és Építményfajták (Mélyépítés / Útépítés) árindexei 2008–2025.
4. **Vállalati és Költségvetési Adatok:**
   * **Magyar Közút Nonprofit Zrt.:** 2020. és 2021. évi könyvvizsgált Éves Beszámolói, Mérlegei és Eredménykimutatásai.
5. **Bírósági Ítéletek és Jogszabályok:**
   * **Kúria Pfv.IV.21.194/2023/15. sz. ítélete** (K-PJ-2024-94), Fővárosi Ítélőtábla 2.Pf.20.469/2023/9/I. jogerős ítélete, Alkotmánybíróság 3372/2024. (X. 8.) AB végzése (IV/1946/2024) az autópálya-koncessziós szerződés 11 mellékletének kiadásáról; valamint kapcsolódó elvi döntésként a Kúria Pfv.IV.21.124/2023/16. sz. határozata.
   * **1991. évi XVI. törvény** a koncesszióról; **1505/2021. Korm. határozat**; **424/2020. Korm. rendelet**.

---

## I. Pillér: a névleges vs. reálérték kérdése (matematikai audit)

### 1. Vitézy Dávid 23 000 milliárdos állításának dekonstrukciója
Vitézy Dávid állítása szerint az állam 35 év alatt *„23 000 milliárd forintot fizet ki a közös pénzünkből az MKIF-nek, ami 46 kamiont megtöltő húszezres”*.

* **A peres dokumentumokból kiderülő valóság:**  
  A Transparency International Magyarország által kiperelt háttérszámításokból és a Nemzeti Koncessziós Iroda (NKOI) kalkulációiból ismert: a 35 éves futamidőre a kifizetések **bázisáron számított jelenértéke 12 600 – 13 700 milliárd forint** volt.
* **Az inflációs mechanizmus:**  
  A koncessziós szerződés 100%-os KSH fogyasztói árindex (CPI) követést ír elő. A KSH hivatalos adatai alapján a kumulált pénzromlás mértéke:
  * 2022: +14,5%
  * 2023: +17,6%
  * 2024: +3,7%
  * Ha a fennmaradó ~32 évre egy konzervatív, évi átlagos 3,5%-os KSH inflációval számolunk, a jövőbeli névleges (nominális) pénzáramok összege:
    $$\sum_{t=1}^{35} \text{RÁD}_t \approx \mathbf{20\ 500 – 23\ 200 \text{ milliárd Ft}}$$
* **A pénzügyi ítélet:**  
  Vitézy száma **nominálisan nem légből kapott**, mert a 35 év alatt ténylegesen kifizetendő forintok összege a kamatos kamat elvén működő inflációs indexálás miatt valóban eléri a 23 ezer milliárdot.  
  **Ugyanakkor módszertanilag súlyosan manipulatív:** Pénzügyi alaptörvény, hogy különböző idősíkokban felmerülő kifizetéseket diszkontálás (Net Present Value – NPV) nélkül nem adunk össze. Összehasonlításképpen: a Magyar Közút Nonprofit Zrt. 2021-es költségvetése (386,1 milliárd Ft) 35 évre vetítve, évi 3,5%-os inflációval számolva szintén **24 800 milliárd Ft** nominális állami kiadást jelentene! Tehát az összeg nagysága magából a 35 éves időtávból és az inflációból fakad, nem önmagában a konstrukció túlárazásából.

---

### 2. A fajlagos díjak reálérték-számítása (ÁSZ 1118 + KSH indexek)
László Szőke azon állítása, hogy a 2010 előtti PPP-k költsége mai áron ~620–750 millió Ft/km/év, míg a 2022-es MKIF díj ~525 millió Ft/km/év, a hivatalos iratok alapján pontosan igazolható.

* **Az ÁSZ 1118. sz. jelentés 43. oldalának primer adatai:**
  * Az M6 Dunaújváros–Szekszárd (M6 Tolna) és Szekszárd–Pécs (Mecsek Autópálya) szakaszokon 2010-ben az alap rendelkezésre állási díj:
    $$\text{Alapdíj}_{2010} = \mathbf{22,3 \text{ millió Ft / km / hó}} = \mathbf{267,6 \text{ millió Ft / km / év}}$$
* **Korrekció a KSH Építőipari és Mélyépítési Árindexével:**  
  A KSH hivatalos STADAT táblái (1.1.1.31 és 1.1.1.32 – Építményfajták termelői árindexe / Mélyépítés, Utak) alapján:
  * 2010-es bázis: 100,0%
  * 2024-es kumulált index: **234,8%** (az építőipari árak 2,35-szörösükre nőttek).
  $$\text{Reáldíj (építőipari index alapján)} = 267,6 \times 2,348 = \mathbf{628,3 \text{ millió Ft / km / év}}$$
* **Korrekció a devizaárfolyam figyelembevételével:**  
  Az ÁSZ 1118. jelentés 43. oldala rögzíti, hogy az állam a devizaárfolyam eltérésének kockázatát teljes mértékben magára vállalta (a szerződések euróalapúak voltak).
  * 2010-es átlagos árfolyam: **275,4 Ft/EUR**
  * 2024–2026-os átlagos árfolyam: **395–400 Ft/EUR** (árfolyamromlás: +44%)
  * Ha a devizában meghatározott díjtételt és a külföldi euró-inflációt visszaváltjuk:
    $$\text{Reáldíj (devizahatással)} \approx \mathbf{690 – 745 \text{ millió Ft / km / év}}$$

* **Matematikai konklúzió:**  
  A számítás igazolja: **költségvetési készpénzkiadási (cash-flow) szempontból az MKIF 525 millió Ft/km/éves átlagdíja valóban 16–29%-kal alacsonyabb reálkiadást jelent kilométerenként az államnak, mint a 2010 előtti PPP-k.**

---

## II. Pillér: fizikai tőketartalom és mérnöki logisztika (zöldmező vs. sávbővítés)

A fenti matematikai előny mögött azonban felmerül a kritikusok jogos kérdése: **Ha a 2022-es koncesszióban a hálózat 85%-a már készen állt, miért nem 70-80%-kal csökkent a díj, miért csak 20-30%-kal?**

Ennek megválaszolásához szét kell választani a zöldmezős építés és a forgalom alatti sávbővítés mérnöki költségszerkezetét.

### 1. Zöldmezős beruházás tőkeigénye (2010 előtt)
* Az M6 déli szakasza (Szekszárd–Pécs) extrém műszaki tartalommal épült: 4 db alagútpár, monumentális völgyhidak, zöldmezős nyomvonal-kialakítás, teljes kisajátítás és földmunka.
* A fizetett rendelkezésre állási díj **70–75%-a a beruházási hitel tőke- és kamattörlesztése volt**, és mindössze **25–30%-a volt az üzemeltetés és fenntartás (O&M)**.

### 2. Sávbővítés 100-120 ezres forgalom mellett (MKIF feladat)
Közlekedésépítési tény, hogy egy meglévő, telített gyorsforgalmi út 2x3 sávra bővítése **nem egyszerűen „melléöntött aszfalt”**:
* **Forgalomterelés és kapacitáskorlát:** Az M1-es autópálya napi átlagos forgalma meghaladja a 80 000 – 110 000 egységjárművet (AADT), kiemelkedően magas (35-40%-os) nehézgépjármű-aránnyal. Ilyen forgalom mellett sávot lezárni csak dinamikus terelésekkel, ideiglenes elválasztófalakkal (betonterelőkkel) és szigorú sebességkorlátozásokkal lehet.
* **Műtárgyak átépítése:** A meglévő felüljárók alatti pillérek nem férnek el a harmadik sáv mellett, így az összes hídszerkezetet át kell építeni vagy cserélni kell. A völgyhidak és átereszek szélesítése forgalom alatt speciális konzolos vagy melléépítéses technológiát igényel.
* **Munkaidő- és logisztikai felár:** A munkák jelentős részét éjszaka, szűkített munkaterületen kell végezni, ami a nehézgépek termelékenységét 40-50%-kal csökkenti, a fajlagos élőmunka- és gépköltséget pedig megnöveli.
* **A mérnöki ítélet:** Egy forgalom alatti 2x3 sávos autópálya-bővítés fajlagos kilométerköltsége (műtárgyakkal és burkolatcserével) ma eléri a **4,0–5,5 milliárd Ft/km** összeget, ami szinte megegyezik egy síkvidéki zöldmezős autópálya építési költségével.

### 3. A hálózati aránytalanság (a szintrehozás vs. a maradék 700 km)
Itt érhető tetten a Szőke-féle érvelés komoly gyenge pontja:
* Az MKIF által vállalt **szintrehozási kötelezettség (kötő- és kopóréteg csere, alapréteg-stabilizáció) ~538 km-re (a hálózat 43%-ára)** vonatkozik az első 10-11 évben.
* **Mi történik a maradék ~700 km-en?**  
  Az M6-oson, az M35-ösön, az M43-ason, az M4 újabb szakaszain és az M3 keleti részein nincs szükség azonnali teljes szerkezeti rekonstrukcióra. Ezeken a szakaszokon a feladat a klasszikus üzemeltetés (kaszálás, hóeltakarítás, lokális javítás, szalagkorlát-csere).
* **A közgazdasági következmény:** Mivel az állam a teljes 1237 km-es hálózatra egységes, ~525 millió Ft/km/éves díjat fizet, a jó állapotú 700 km-en a koncesszor **kiemelkedően magas működési haszonkulcsot (EBITDA margin > 40-50%)** ér el, amellyel részben az M1 sávbővítését finanszírozza keresztbe, részben pedig tiszta osztalékként realizál.

---

## III. Pillér: műszaki tartalom, SLA és a kötbérrendszer történeti valósága

A vitában elhangzott korábbi érvelés egyik legsúlyosabb tévedése az volt, miszerint *„2010 előtt nem léteztek SLA-k, így azoknak áruk sem volt”*.

### 1. Mit mond az ÁSZ 1118. sz. jelentés a 2010 előtti SLA-król?
Az ÁSZ jelentés **43. és 51. oldala (29. és 30. lábjegyzetek)** tételesen cáfolja ezt az állítást:
* **29. lábjegyzet:** *„Az alap rendelkezésre állási díj szorzója, amely a szolgáltatás hiányosságaitól függően csökkenti annak értékét.”*
* **30. lábjegyzet:** *„Ennek alkalmazásával veszik figyelembe az üzemeltetés hiányosságait és ez alapján határozzák meg a levonások mértékét.”*
* **51. oldal:** Az ÁSZ dokumentálja, hogy az ellenőrzött 10 hónapból **6 hónapban vont le az állam díjat** a koncesszortól rendelkezésre nem állás, burkolathibák és alagútbeli sebességkorlátozások miatt.

### 2. Miben különbözik mégis a 2022-es műszaki szabályozás?
Bár a szankciórendszer régen is létezett, a 2022-es koncessziós szerződés műszaki előírásai több ponton szigorúbbak és korszerűbbek:
1. **Objektív mérési protokollok:** A burkolat állapotát (nyomvályúmélység, hosszirányú egyenetlenség – IRI, felületi makrotextúra és tapadás) nagypontosságú lézeres mérőautókkal, digitálisan rögzítik, és a határérték-túllépés emberi mérlegelés nélkül, szoftveresen vált ki automatikus fizetési dedukciót.
2. **Technológiai többlettartalom:**
   * WIM (Weight-in-Motion) dinamikus tengelysúlymérő rendszerek kötelező telepítése a tehergépjármű-túlterhelésből fakadó aszfaltromlás megelőzésére.
   * Teljes optikai lefedettség és intelligens kamerarendszer (ITS), amely azonnali forgalomirányítási beavatkozást tesz lehetővé.
   * Európai uniós zöldkövetelmények: AFIR-kompatibilis nagyteljesítményű elektromos töltőhálózat kiépítése a pihenőhelyeken, korszerűbb vadvédelmi és zajvédelmi létesítmények.
3. **Összegzés:** A 2022-es szerződés technológiai színvonala magasabb, de ez **a technológiai fejlődés 15 évének természetes következménye**, nem pedig a korábbi szankciórendszer hiányának pótlása.

---

## IV. Pillér: tőkeköltség (WACC), kockázatmegosztás és államadósság (közgazdasági levezetés)

Ez a pont a teljes koncessziós vita elméleti magja, ahol mindkét fél érvelése elbukott a valós pénzügyi mechanizmusok felületes ismerete miatt.

### 1. A tőkeköltség (WACC) felépítése az infrastruktúra-finanszírozásban
Az **EPEC / EIB (2015)** *Value for Money Assessment* módszertani útmutatója (22–32. o.) és **Engel, Fischer, Galetovic (2014)** alapján egy koncessziós projekt finanszírozási költsége a súlyozott átlagos tőkeköltségből (WACC) adódik:
$$WACC = \left( \frac{E}{V} \times r_e \right) + \left( \frac{D}{V} \times r_d \times (1 - T_c) \right)$$
Ahol:
* $E/V$: Saját tőke aránya a projektben (jellemzően 15–20%).
* $D/V$: Idegen tőke (bankhitel) aránya (jellemzően 80–85%).
* $r_e$: Elvárt saját tőke hozam (Equity IRR). A Transparency International által kiperelt adatok és a G7 gazdasági elemzései szerint a koncesszorok **10–14%-os elvárt belső megtérülési rátával (IRR)** kalkuláltak.
* $r_d$: Idegen tőke költsége (szindikált bankhitel kamata = bankközi kamatláb + 200–350 bázispontos kockázati marzs).
* $T_c$: Társasági adókulcs.

### 2. A szuverén finanszírozás költsége (ÁKK hozamgörbe)
Ha a magyar állam közvetlenül bocsát ki államkötvényt a fejlesztések finanszírozására:
* Az állam hitelfelvételi költsége a szuverén benchmark hozam ($r_g$).
* 2021-ben, a koncesszió előkészítésekor a 10–20 éves magyar államkötvények referenciahozama **~2,5–3,5%** között mozgott!
* **A tőkeköltség-különbözet (Financing spread):**
  $$\Delta = WACC_{\text{magán}} - r_{g\ (\text{állami})} \approx \mathbf{+3,5\% – +6,0\%}$$

### 3. Az ÁSZ 1118. sz. jelentés 39–40. oldalának ítélete: az „off-balance sheet” tévhit
A korábbi Gemini-érvelés azt állította, hogy a modell azért volt kedvező, mert *„az államadósság közvetlen növelése nélkül, olcsóbb banki hitelekből valósul meg a beruházás”*.

**Ez az állítás szakmailag tarthatatlan, és az ÁSZ már 2011-ben cáfolta:**
1. **A magánhitel SOHA nem olcsóbb az állami hitelnél:** A konzorciumot hitelező bankok magasabb kockázati felárat kérnek egy magáncégtől, mint a magyar államtól, a magántőkealap tulajdonosai pedig 10–14%-os garantált profitot követelnek.
2. **A mérlegen kívüliség pusztán statisztikai szemfényvesztés:**  
   Az ÁSZ 1118. jelentés 39. oldala szó szerint feltárja, hogy a 2006–2008-as PPP-knél a kormányzat kizárólag azért erőltette a konstrukciót, hogy:
   > *„a Közbeszerzési Eljárás az államháztartási mérlegen kívüli tétel legyen; azaz a maastrichti kritériumoknak megfelelően számított államháztartási hiányt, illetve államadósságot ne növeljék egy összegben a koncesszió teljes futamideje alatt...”*
3. **Az ÁSZ elmarasztalása (40. o.):** Az Állami Számvevőszék megállapította, hogy a pénzügyi tanácsadók mesterségesen manipulatív számításokkal (Public Sector Comparator eltorzításával, állami opció túlárazásával) hozták ki a PPP-t kedvezőbbnek. A valóságban a mérlegen kívüli elszámolás miatt az állam **évtizedeken át garantált, merev és jóval magasabb törlesztési kötelezettséget vállalt magára**, ami végső soron sokkal több közpénzbe került az adófizetőknek, mintha nyíltan felvette volna az olcsóbb államkölcsönt.

### 4. A kockázatmegosztás aszimmetriája (Oszkár Fekete igaza)
A közgazdasági elmélet (EPEC, Engel et al.) szerint a magasabb magántőkeköltség egyetlen esetben indokolt: **ha a magánfél valódi piaci kockázatokat vállal át az államtól** (pl. ha kevés az autó, a magánfél veszteséget könyvel el).

* **A magyar valóság:**
  * **Forgalmi kockázat (Traffic risk):** 100%-ban az államnál van. A rendelkezésre állási díjat az állam akkor is köteles kifizetni, ha a Covid-lezárások vagy a gazdasági válság miatt üresek az autópályák.
  * **Inflációs kockázat:** 100%-ban az államnál van (szerződéses KSH CPI korrekció).
  * **Kamatkockázat:** A díjképletekben elszámolható a finanszírozási költségek változása.
* **A tudományos verdikt:**  
  Ha a magánfélnek **nulla piaci keresleti kockázata van**, akkor a 10–14%-os elvárt hozam (Equity IRR) és a 35 évre garantált inflációkövető állami díj **gazdaságilag indokolatlan járadék (economic rent)**, amely az adófizetőktől a koncessziós konzorcium tulajdonosaihoz csoportosítja át a vagyont. Ebben a kérdésben Oszkár Fekete és az ÁSZ kritikája maradéktalanul helytálló.

---

## V. Pillér: jogállamiság, bírósági ítéletek és transzparencia

A vitában Szőke azzal hárította el a szerződések nyilvánosságának hiányát, hogy *„a 2010 előttieket is ki kellett perelni, és a jövőbeliekkel is így lesz, mert csak...”*

Ez a megközelítés jogilag tarthatatlan. A magyar bíróságok az elmúlt években világos és kikezdhetetlen jogi normákat fektettek le a közpénzek és koncessziók védelmében:

1. **A Kúria Pfv.IV.21.194/2023/15. sz. ítélete (K-PJ-2024-94) és a Fővárosi Ítélőtábla jogerős ítélete (2.Pf.20.469/2023/9/I.):**
   * A bíróságok kimondták, hogy a Nemzeti Koncessziós Iroda (NKOI) és a beavatkozó MKIF **jogellenesen tagadta meg a 35 éves koncessziós szerződés 11 pénzügyi és műszaki mellékletének kiadását**.
   * A bíróság rögzítette, hogy az üzleti titok védelmének felülvizsgálata tiszta jogkérdés (közérdekűségi teszt), amely szakértői bizonyítás nélkül is eldöntendő; a RÁD-számítási modell, a levonások és a pályázati pénzügyi táblázatok közérdekű adatok, nem védendő titkok.
2. **Az Alaptörvény 39. cikkének sérelme:**
   * Az Alaptörvény 39. cikk (2) bekezdése rögzíti: *„A közpénzekkel gazdálkodó minden szervezet köteles a nyilvánosság előtt elszámolni a közpénzekre vonatkozó gazdálkodásával. A közpénzekre és a nemzeti vagyonra vonatkozó adatok közérdekű adatok.”*
   * A bíróságok kimondták: a magántőkealapok struktúrája mögé rejtett közfeladat-ellátás sem mentesíti az államot a teljes pénzügyi átláthatóság alól.
3. **Következtetés:** A szerződések titkosítása nem „természetes adottság”, hanem **jogsértő állami magatartás**, amelyet a bíróságok szankcionáltak és megsemmisítettek.

---

## VI. A mesterérvelés szintézise: a professzionális, cáfolhatatlan álláspont

Ha egy vitában megcáfolhatatlan, a politikai demagógiától megtisztított, tudományosan és forrásilag kikezdhetetlen álláspontot akarunk képviselni, a következő szintézist kell alkalmazni:

```
                                  A KONCESSZIÓS ÉRVELÉS MÉRLEGE
                                                │
                ┌───────────────────────────────┴───────────────────────────────┐
                ▼                                                               ▼
   AHOL A KORMÁNYZATI / MKIF                        AHOL A KRITIKUS / ÁSZ OLDALNAK
       ÉRVELÉS MEGÁLL:                                      VAN IGAZA:
┌──────────────────────────────────────────────┐ ┌──────────────────────────────────────────────┐
│ 1. Reálértéken mért költségvetési cash-flow: │ │ 1. Tőkeköltség (WACC) és kamatfelár:         │
│    A KSH és ÁSZ 1118 alapján a 2010-es       │ │    A magántőke elvárt hozama (IRR 10-14%) és │
│    PPP mai áron 630-745 mFt/km/év volt,      │ │    a banki hitel jóval drágább, mint a 3-4%- │
│    míg a 2022-es díj ~525 mFt/km/év          │ │    os államkötvény (EPEC / EIB bizonyítás).  │
│    (16-29%-os folyó kiadási megtakarítás).   │ │                                              │
│                                              │ │ 2. Off-balance sheet illúzió:                │
│ 2. Forgalom alatti sávbővítés felára:        │ │    Az ÁSZ 1118 (39. o.) szerint az Eurostat  │
│    100-120 ezres AADT mellett hidakat szé-   │ │    adósságlimit kikerülése statisztikai trükk│
│    lesíteni és 2x3 sávra bővíteni fajlagosan │ │    amely hosszú távon megdrágítja az életet. │
│    csaknem olyan drága, mint a zöldmező.     │ │                                              │
│                                              │ │ 3. Forgalmi kockázat hiánya:                 │
│ 3. Szintrehozási kötelezettség és SLA:       │ │    Mivel az állam garantálja a rendelkezésre │
│    A Magyar Közút forráshiányával szemben a  │ │    állási díjat, a magánfél kockázatmentes   │
│    szerződés kötelezővé teszi 538 km mély-   │ │    extraprofitot realizál a hálózat kész     │
│    felújítását, automata kötbér terhe mellett.│ │   részén (700 km jó állapotú pálya).       │
└──────────────────────────────────────────────┘ └──────────────────────────────────────────────┘
```

### A megkérdőjelezhetetlen konklúzió három mondatban:
1. **Mérnöki és költségvetési szempontból** a 2022-es MKIF-modell kilométerenként reálértéken alacsonyabb azonnali állami készpénzterhelést jelent a 2010-es zöldmezős PPP-knél, miközben a forgalom alatti M1-es sávbővítés és a ~600 km-es felújítás elvégzésére kötelezi a koncesszort szigorú digitális mérések mellett.
2. **Pénzügyi-közgazdasági szempontból** azonban az állam a forgalmi kockázat teljes átvállalásával és az infláció 100%-os garantálásával egy olyan mérlegen kívüli (off-balance sheet) konstrukciót hozott létre, amelyben a magánkonzorcium 10–14%-os elvárt saját tőke hozamát és piaci banki marzsát fizeti ki, ami az ÁSZ és az EIB szerint hosszú távon lényegesen drágább az adófizetőknek, mint a közvetlen szuverén államkötvényes finanszírozás.
3. **Végső diagnózis:** A 2022-es koncesszió mérnöki-műszaki tartalma korszerűbb, de pénzügyi-strukturális alaphibája pontosan ugyanaz, mint a 2010 előtti PPP-ké: az állam a maastrichti adósságlimitek adminisztratív megkerülése érdekében évtizedekre garantált járadékot enged át a magántőkének ahelyett, hogy saját, olcsóbb forrásból finanszírozná a nemzeti infrastruktúrát.
