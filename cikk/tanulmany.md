# A magyar gyorsforgalmi úthálózat koncessziós rendszerének komplex mérnöki, pénzügyi és közpolitikai elemzése

**Dátum:** 2026. szeptember 22.  
**Tárgy:** Az MKIF 2022-es koncessziós szerződésének és a 2010 előtti gyorsforgalmi PPP-modelleknek (M5, M6) az összehasonlító elemzése primer hatósági, számvevőszéki és bírósági dokumentumok, valamint nemzetközi tőkeköltség-szakirodalom alapján.

---

## 1. Forráskritikai alapvetés és módszertan

A gyorsforgalmi úthálózat finanszírozási modelljeinek megítélése a hazai gazdaságpolitikai diskurzus egyik leginkább polarizált kérdése. Jelen elemzés célja a 2010 előtti autópálya PPP-konstrukciók (különösen az M5 és M6/M60 projektek) és a 2022-ben 35 évre megkötött gyorsforgalmi koncessziós rendszer objektív, számszerűsíthető és dokumentumokon alapuló összevetése.

A módszertani tisztesség megköveteli a felhasznált forráskategóriák szigorú szétválasztását és kritikáját:

1. **Primer jogforrások és bírósági ítéletek:** A koncesszióról szóló 1991. évi XVI. törvény; az 1505/2021. (VII. 29.) Korm. határozat; a Nemzeti Koncessziós Irodát (NKOI) létrehozó 424/2020. (IX. 10.) Korm. rendelet; a Fővárosi Törvényszék `25.P.21.778/2023/18.` számú kijavított ítélete; a Fővárosi Ítélőtábla `2.Pf.20.469/2023/9/I.` számú jogerős ítélete; a Kúria `Pfv.IV.21.194/2023/15.` számú felülvizsgálati ítélete (azonosító: `K-PJ-2024-94`); valamint az Alkotmánybíróság `3372/2024. (X. 8.) AB végzése` (`IV/1946/2024`)[^1].
2. **Hivatalos számvevőszéki és statisztikai adatok:** Az Állami Számvevőszék 1118. számú jelentése a 2009–2010-ben befejeződő autópálya-beruházásokról és pénzügyi folyamataikról; az ÁSZ 1003. számú jelentése a gyorsforgalmi úthálózati szervezetrendszerről; valamint a Központi Statisztikai Hivatal (KSH) STADAT 1.1.1.2. (fogyasztói árindex) és STADAT 1.1.1.32. (építményfajták, utak és autópályák termelői árindexe) hivatalos táblái[^2].
3. **Könyvvizsgált vállalati beszámolók és hivatalos vállalati közlések:** A Magyar Közút Nonprofit Zrt. 2020. és 2021. évi auditált beszámolói; az MKIF Magyar Koncessziós Infrastruktúra Fejlesztő Zrt. hivatalos adatai a vállalt 538 km-es szintrehozási programról és a kezelésbe vett 1237 km-es hálózatról; valamint a konzorcium magántőkealap-struktúrájára, alapkezelőire és végső gazdasági érdekeltségeire vonatkozó nyilvános cégbírósági és sajtóadatok[^3][^5].
4. **Nemzetközi módszertani útmutatók és lektorált szakirodalom:** Az Európai Beruházási Bank (EIB) és az EPEC (European PPP Expertise Centre) tőkeköltség- és Value for Money (VfM) módszertana; a brit HM Treasury *Green Book* útmutatója; valamint Voszka Éva és Major Iván tanulmányai a Közgazdasági Szemlében[^4].
5. **Szakértői mérnöki és pénzügyi becslések:** A forgalom alatti 2x3 sávos kapacitásbővítés fajlagos költségmodelljei és a piaci tőkeköltség (WACC) érzékenységi elemzései.

---

## 2. A névleges és a reálérték vizsgálata: a matematikai audit

### 2.1. A 23 000 milliárd forintos állítás dekonstrukciója és diszkontálási modellje

A nyilvános vitában elterjedt tétel, miszerint a magyar állam 35 év alatt mintegy 23 000 milliárd forintot fizet ki az MKIF-nek, a kumulált nominális pénzáramok szintjén reális nagyságrendet jelez, azonban pénzügytanilag önmagában nem tekinthető a konstrukció tőkeértékének. A kormányzat 2026. szeptemberi közlése 23 196 milliárd forintos teljes, 35 évre számított nominális fizetési kötelezettséget említ. Egyes sajtóelemzések (24.hu) a szerződésmódosítások és többletfeladatok (különösen az M1 kapacitásbővítésének átadása) figyelembevételével ennél magasabb, akár 25 900 milliárd forintos kifizetési keretet becsülnek. A két adat nem tekinthető automatikusan azonos tartalmú mutatónak: eltérhetnek a számításba bevont pénzáramok, az időpont és az inflációs feltételezések. Ezeket ezért csak egységes szerződéses pénzáram-modell alapján lehet közvetlenül összehasonlítani.

Közgazdasági alapszabály, hogy különböző időpontokban felmerülő kifizetések nem adhatók össze egyszerűen, hanem azokat jelenértékre kell diszkontálni. Ha a tényleges infláció az egyes években eltérő ($\pi_i$), és a diszkontráta is igazodik ehhez ($r_{n,i}$), a diszkrét idejű jelenérték-számítás pontos képlete:

$$
\text{PV} = \sum_{t=1}^{35} \frac{\text{RÁD}_0 \prod_{i=1}^{t} (1 + \pi_i)}{\prod_{i=1}^{t} (1 + r_{n,i})}
$$

A nominális pénzáramok diszkontálásánál a Fisher-féle összefüggést kell alkalmazni a nominális diszkontráta ($r_{n,i}$), a reál diszkontráta ($r_{r,i}$) és az adott évi infláció ($\pi_i$) között:

$$
1 + r_{n,i} = (1 + r_{r,i})(1 + \pi_i)
$$

Ha a reál diszkontráta a futamidő alatt állandó ($r_{r,i} = r_r$), a szorzatok egyszerűsödnek: az inflációs tényezők kiejtik egymást, és a modell visszavezethető a bázisáras reálértékű pénzáramok reálkamatlábbal történő diszkontálására:

$$
\text{PV} = \sum_{t=1}^{35} \frac{\text{RÁD}_0 \prod_{i=1}^{t} (1 + \pi_i)}{\prod_{i=1}^{t} (1 + r_r)(1 + \pi_i)} = \sum_{t=1}^{35} \frac{\text{RÁD}_0}{(1 + r_r)^t} = \text{RÁD}_0 \times A_{35, r_r}
$$

Ahol $A_{35, r_r} = \frac{1 - (1 + r_r)^{-35}}{r_r}$ a 35 éves annuitási faktor.

Fontos módszertani korlát azonban, hogy az infláció semlegesítése csak a teljes egészében, azonos indexszel indexált RÁD-komponensre vonatkozik. A fejlesztési díjak, részlegesen indexált költségek, fix kamatozású finanszírozás, adók és szerződésmódosítások esetében külön nominális cash-flow-modellezés szükséges.

Szemléltető példaként (kizárólag az exponenciális növekedés és a több évtizedes nominális összeadások torzító hatásának illusztrálására): a Magyar Közút Nonprofit Zrt. 2021. évi beszámolóiban szereplő, mintegy 386 milliárd forintos bevételi és költségvetési támogatási nagyságrendet — kizárólag szemléltető jelleggel — 35 évre, évi 3,5%-os indexálással felfuttatva mintegy **26 640 milliárd forintot** tenne ki (illetve év eleji kifizetési konvencióval mintegy 25 740 milliárd forint kumulált összeget adna):

$$
\sum_{t=1}^{35} 386 \times 1,035^t = 386 \times 1,035 \times \frac{1,035^{35}-1}{0,035} \approx \text{\textbf{26 640 milliárd Ft}}
$$

Fontos rögzíteni, hogy ez a példa nem tekinthető a koncesszió közvetlen benchmarkjának, mivel a Magyar Közút a teljes 32 000 km-es országos úthálózatot kezeli és eltérő feladatokat lát el, csupán azt szemlélteti, hogy 35 év távlatában a nominális összeadások miként torzítják a nominális költségérzékelést.

### 2.1.1. Számítási modellek és jelenérték-szimulációk

**1. Kumulált nominális kifizetés a tényleges inflációval** (KSH fogyasztói árindex tényadatok: CPI 2022 = 14,5%, CPI 2023 = 17,6%, CPI 2024 = 3,7%), majd a fennmaradó futamidőre feltételezett hosszú távú inflációval ($\pi = 3,5$%):

$$
\sum_{t=1}^{35} \text{RÁD}_t = \sum_{t=1}^{35} \left[ \text{RÁD}_0 \prod_{i=1}^t (1 + \pi_i) \right] \approx \text{\textbf{20 500 – 23 200 milliárd Ft}}
$$

**2. Inflációtól semlegesített reálértékű annuitás érzékenysége a reál diszkontrátára** ($\text{RÁD}_0 = 375 \text{ Mrd Ft}$ bázis üzemeltetési díj mellett):

| Reál diszkontráta ($r_r$) | Várható infláció ($\pi = 2,5$%) | Várható infláció ($\pi = 3,5$%) | Várható infláció ($\pi = 5,0$%) | Annuitási szorzó ($A_{35, r_r}$) | Reál jelenérték (NPV) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$r_r = 1,5$%** | 10 030 Mrd Ft | 10 030 Mrd Ft | 10 030 Mrd Ft | 26,75 | **10 030 Mrd Ft** |
| **$r_r = 2,5$%** | 8 680 Mrd Ft | 8 680 Mrd Ft | 8 680 Mrd Ft | 23,15 | **8 680 Mrd Ft** |
| **$r_r = 3,5$%** | **7 500 Mrd Ft** | **7 500 Mrd Ft** | **7 500 Mrd Ft** | **20,00** | **7 500 Mrd Ft** |
| **$r_r = 4,5$%** | 6 560 Mrd Ft | 6 560 Mrd Ft | 6 560 Mrd Ft | 17,49 | **6 560 Mrd Ft** |

*Megjegyzés:* A táblázat oszlopaiban az értékek megegyeznek, mert a Fisher-összefüggés alapján a 100%-ban CPI-indexált pénzáramok és a nominális diszkontráta inflációs prémiuma teljesen semlegesíti egymást. Ha a költségek egy része fix forintkamatú hitel, az infláció emelkedése reálértéken devalválja a tőketartozást, növelve a koncesszor járadékát.

**3. A jelenérték lehetséges komponenseinek indikatív rekonstrukciója** (3,5%-os reál diszkontráta mellett):
*Módszertani megjegyzés:* A táblázat szigorúan szétválasztja a költségvetési szerződéses cash flow-t (mit fizet közvetlenül az állam) és a magánfinanszírozási modell közgazdasági többletterhét (WACC-felár). A finanszírozási tétel nem része a költségvetési szerződéses NPV-nek; közgazdasági többletköltségként csak külön modellben adható hozzá.

| Pénzáram-komponens | Bázisérték / Éves ráfordítás | Szerződéses mechanizmus és pénzügyi tartalom | Időtáv | Becsült jelenérték (NPV) |
| :--- | :--- | :--- | :---: | :---: |
| **I. Költségvetési szerződéses kifizetések** | | | | |
| **Alap RÁD** | ~360 – 390 Mrd Ft / év | Üzemeltetés és rutinfenntartás szerződéses alapdíja (CPI-követő) | 35 év | ~7 200 – 7 800 Mrd Ft |
| **RÁASZD (Szintrehozási díj)** | ~60 – 80 Mrd Ft / év | 538 km gyorsított felújításának tőketörlesztési díjeleme | 1–11. év | ~600 – 800 Mrd Ft |
| **Fejlesztési díjak (M1 bővítés)** | Célzott beruházási mérföldkövek | Forgalom alatti 2x3 sávos bővítés, hidak, csomópontok beruházási díjai | 1–10. év | ~2 800 – 3 500 Mrd Ft |
| **Költségvetési szerződéses NPV összesen** | — | **Közvetlen állami fizetési kötelezettség jelenértéke:** | **35 év** | **~10 600 – 12 100 Mrd Ft** |
| **II. Finanszírozási és közgazdasági modell** | | | | |
| **Finanszírozási modellből származó többletköltség** | Indikatív tőkeköltség-prémium | A koncesszor finanszírozási struktúrájából, tőkeáttételéből, tartalékszámláiból (DSRA) és WACC-felárából származó becsült közgazdasági többletteher; nem azonos a költségvetési szerződéses kifizetéssel | 35 év | ~1 200 – 1 800 Mrd Ft |
| **Teljes közgazdasági erőforrás-ráfordítás** | — | **Szerződéses NPV + indikatív magántőke finanszírozási prémium:** | **35 év** | **~11 800 – 13 900 Mrd Ft** |

---

### 2.2. A fajlagos kilométerdíjak reálérték- és árfolyam-korrekciós összevetése

A 2010 előtti PPP-k és a 2022-es koncesszió díjainak összehasonlításakor a nominális kilométerköltség közvetlen összevetése súlyos módszertani hiba lenne. Az ÁSZ 1118. számú jelentésének 43. oldala rögzíti, hogy az M6 Tolna és Mecsek szakaszokon a 2010. évi bázison az alap rendelkezésre állási díj havi összege 22,3 millió Ft/km volt (évi 267,6 millió Ft/km/év). 

A reálértékre történő átszámításnál el kell kerülni a kettős indexálás csapdáját (amikor a forintösszegre egyszerre teszik rá a hazai árindexet és a devizaleértékelődést). Két eltérő, összehasonlító célú korrekciós módszer alkalmazható:

1. **Belföldi építőipari termelői árindex (KSH):** A KSH STADAT 1.1.1.31. táblája (Egyéb építmények / Mélyépítés) és 1.1.1.32. táblája (Utak, autópályák építése alcsoport) alapján a kumulált árindex a hivatalos éves láncindexek szorzatával határozható meg:

$$
I_{2010\to2024} = \prod_{t=2011}^{2024} \frac{\text{Index}_t}{100}
$$

Fontos rögzíteni, hogy a 2,348 és 2,438 értékeket a KSH nem egyetlen statikus adatként publikálja, hanem azok a közzétett éves termelői árindexekből képzett kumulatív mutatószámok. A mélyépítési termelői árindex kumulált szorzója $2,348$ (+134,8%-os áremelkedés), míg a kifejezetten az utak alcsoportra vonatkozó index szorzója $2,438$ (+143,8%). Ezzel a 2010-es bázisdíj mai megfelelője 628,3 és 652,4 millió Ft/km/év közé esik.
2. **Szerződéses deviza- és uniós árindex:** Az ÁSZ 1118. jelentés szerint az M6-os díjak devizában (EUR) voltak rögzítve, és az árfolyamkockázatot az állam viselte. A 2010-es 275,4 Ft/EUR árfolyamon az akkori díj mintegy 971 700 EUR/km/év volt. Ha erre az európai mélyépítési inflációt (~145%) és a mai euróárfolyamot (~395 Ft/EUR) alkalmazzuk, az eredmény 556,5 millió Ft/km/év.

Az ismert éves keretből visszaszámított, mintegy 525 millió Ft/km/év indikatív induló átlag nem közvetlenül a teljes szerződésből kiolvasott homogén alapdíj, hanem az ismert éves keret és az 1237 km-es induló hálózat hányadosaként képzett indikatív átlag és visszaszámított becslés. Az elemző sajtó (a G7 2022. májusi és a Telex 2022. júniusi feltáró cikkei) a 2022/2023-as központi költségvetési törvényjavaslatok és az NKOI fejezeti előirányzatai alapján az éves bruttó kifizetési keret (~650 milliárd forint) áfamentes, nettó üzemeltetési és rendelkezésre állási hányadából számította ki ezt az indikatív fajlagos nagyságrendet az 1237 km-es hálózatra vetítve.

A két eltérő, egyaránt indokolható indexálási módszer 525 és 628 millió (illetve 652 millió), valamint 525 és 557 millió forint/km/év közötti összevetési tartományt ad. Ez nem bizonyítja önmagában az MKIF költségelőnyét, csak azt mutatja, hogy az eredmény erősen függ az alkalmazott indexálási konvenciótól és az árfolyamkezeléstől. Emellett alapvető különbség van a fizikai tőketartalomban: az M6-nál az állam új zöldmezős sztrádát kapott alagutakkal, míg az MKIF-nél a meglévő hálózat üzemeltetését és szintrehozását fizeti.

### 2.2.1. Részletes számítási levezetés és módszertani összevetés

$$
\text{Alapdíj}_{2010} = 22,3 \text{ millió Ft / km / hó} = \mathbf{267,6 \text{ millió Ft / km / év}}
$$

**1. Módszer: KSH építőipari termelői árindexek levezetése** (2010=100 bázisra újrabázisolt szerzői értékek, $2010 \to 2024$ láncszorzat):

| KSH STADAT Kategória | 2010 bázis | 2015 szint | 2020 szint | 2024 kumulált szorzó ($I$) | Számított mai fajlagos díj |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mélyépítés (1.1.1.31)** | 100,0% | 108,4% | 148,2% | **2,348** (+134,8%) | $267,6 \times 2,348 = \text{\textbf{628,3 M Ft/km/év}}$ |
| **Utak alcsoport (1.1.1.32)** | 100,0% | 107,9% | 151,6% | **2,438** (+143,8%) | $267,6 \times 2,438 = \text{\textbf{652,4 M Ft/km/év}}$ |

*Módszertani megjegyzés:* A táblázatban szereplő értékek a KSH hivatalos éves láncindexeinek kumulált szorzatai 2010=100-as újrabázisolással. A KSH nem közvetlenül ilyen több évtizedes összefüggő indexeket közöl; a számítás a mélyépítési és útépítési alágazati módszertan folytonosságának feltételezésével készült.

**2. Módszer: Szerződéses euróalap és devizaárfolyam-korrekció:**

$$
\text{Díj}_{2010, \text{EUR}} = \frac{267,6 \text{ millió Ft}}{275,4 \text{ Ft/EUR}} \approx 971\ 700 \text{ EUR / km / év}
$$

$$
\text{Reáldíj}_{\text{EUR/HUF}} = 971\ 700 \times 1,45 \times 395 \text{ Ft/EUR} \approx \mathbf{556,5 \text{ millió Ft / km / év}}
$$

Az ismert éves keretből visszaszámított, mintegy 525 millió Ft/km/év indikatív induló átlaghoz viszonyított relatív különbség:

$$
\Delta_{\text{mélyépítés}} = \frac{525 - 628,3}{628,3} \approx \text{\textbf{-16,4\%}}, \quad \Delta_{\text{EUR}} = \frac{525 - 556,5}{556,5} \approx \text{\textbf{-5,7\%}}
$$

---

## 3. Fizikai tőketartalom és mérnöki logisztika

### 3.1. Zöldmezős beruházás versus forgalom alatti kapacitásbővítés

A reálérték-számítás rámutat a folyó költségvetési kiadás mérsékeltebb voltára, ám a tőkeérték vizsgálata rávilágít a két modell közötti mély szerkezeti különbségre. 2010 előtt a magasabb kilométerdíjért cserébe az állam új, zöldmezős infrastruktúrát kapott: az M6 déli szakaszán 4 alagútpárt, völgyhidakat és teljes nyomvonal-kialakítást. Ezzel szemben a 2022-es koncesszióban átadott 1237 kilométernyi induló hálózat döntő többsége (mintegy 85%-a) már a koncesszió előtt megépült (vegyes forrásokból: hazai költségvetés, európai uniós kohéziós támogatások és korábbi hitelstruktúrák révén), így a koncessziós díj nem egy teljes egészében zöldmezős hálózat létrehozásának tőkeköltségét tükrözi.

Mérnöki szempontból ugyanakkor a meglévő pálya forgalom alatti 2x3 sávos kapacitásbővítése (mint az M1 esetében) jelentős technológiai és logisztikai felárral jár a zöldmezős építéshez képest. Az M1-es autópálya 80 000 – 110 000 jármű/nap forgalomterhelése mellett végzett szélesítésénél a keresztező felüljárók pillérei korlátozzák a pályatestet (több tucat híd teljes átépítése vagy cseréje szükséges), a völgyhidak szélesítése egyedi mérnöki szerkezeteket igényel, míg a folyamatos sávelhúzások, beton terelőfalak és éjszakai munkavégzés mintegy 30–50%-kal csökkentik a nehézgépek napi termelékenységét.

### 3.1.1. Indikatív mérnöki költségmodell és költségszintek

Indikatív mérnöki költségmodell forgalom alatti 2x3 sávos autópálya-bővítésre (összevetve a MAÚT irányelvekkel és a hazai gyorsforgalmi közbeszerzési referencia-árakkal):

$$
C_{\text{bővítés}} = C_{\text{pályaszerkezet}} + C_{\text{műtárgy-átépítés}} + C_{\text{terelés}} + C_{\text{logisztikai-felár}}
$$

*Megjegyzés:* A komponensek nem feltétlenül additív, egymástól teljesen független költségsorok; a modell strukturális bontásként, nem végleges költségvetésként értelmezendő.

Ahol az indikatív szakértői becslés és mérnöki benchmark költségszintek:
* **Közvetlen pályaszerkezeti és alépítményi bővítés:** **4,0 – 5,5 milliárd Ft / km** (pályatest szélesítése, új kopó- és kötőrétegek, alapozás).
* **Teljes projektköltségű mérnöki referencia (All-in):** A kormányzati és sajtóbeszámolókban az M1 mintegy 78 km-es (az M0 autóút és Győr közötti) szakaszára megjelent 620–800 milliárd forintos teljes keretösszeg fajlagosan **7,9 – 10,3 milliárd Ft / km** költségszintet jelent (folyó áron, a felüljárók és hidak teljes újjáépítésével, a különszintű csomópontok kapacitásbővítésével, ITS-rendszerrel, zajvédelemmel és a forgalom alatti terelés logisztikai többletterheivel együtt).
* **Zöldmezős összehasonlító referencia:** Az elmúlt években megvalósult új, 2x2 sávos síkvidéki zöldmezős szakaszok (pl. M44, M4 Abony–Törökszentmiklós) ára 3,8–4,8 milliárd Ft/km volt, míg a műtárgyigényes hegyvidéki nyomvonalak (pl. M30 Miskolc–Tornyosnémeti) ára elérte az 5,2–5,8 milliárd Ft/km szintet.

*Módszertani megjegyzés:* A 4,0–5,5 milliárdos közvetlen pályaszerkezeti becslés és a 7,9–10,3 milliárdos all-in projektkeret eltérő költségdefiníciót használ (közvetlen kivitelezési ráfordítás vs. teljes beruházási program), ezért nem tekinthetők közvetlen ár-összehasonlításnak.

---

### 3.2. A hálózati aránytalanság, az ütemezés és a keresztfinanszírozási modell

A koncessziós csomag közgazdasági logikájának megértéséhez elengedhetetlen a felújítási feladatok ütemezésének és műszaki mélységének szétválasztása:
1. **Gyorsított szintrehozási program (2022–2025):** Az MKIF az első 3 évben a legsúlyosabban leromlott burkolatú szakaszokon mintegy 538 kilométeren (a hálózat ~43%-án) hajt végre nagyfelületű aszfaltozást, marást és kötőréteg-cserét.
2. **Ciklikus mélyfelújítási program (10–11 éves szerződéses ciklus):** A szerződéses életciklus-kötelezettségek a teljes hálózat állapotfenntartását és a szükséges rekonstrukciókat írják elő; ezek nem minden szakaszon azonos mélységű beavatkozást jelentenek, hanem a burkolati és mérnöki diagnosztika függvényében a szükséges mélyszerkezeti felújítást és a műtárgyak állapotjavítását írják elő a futamidő alatt.

A hálózat mintegy 700 kilométernyi szakasza (például a nemrég átadott M35, M43 vagy a 2010 után épült M4 szakaszok) jelenleg kiváló műszaki állapotban van, így ezeken a kezdeti években csupán rutinüzemeltetés és fenntartás szükséges. Mivel az állam a teljes 1237 km-es hálózatra egységes rendelkezésre állási díjat fizet, a díjcsomag hálózati szintű átlagolása megteremtheti a hálózaton belüli keresztfinanszírozás lehetőségét, amelynek tényleges mértéke a projektcégek belső költség- és bevételallokációja nélkül pontosan nem számszerűsíthető.

---

## 4. Műszaki tartalom, szolgáltatási szintek és a kötbérrendszer

### 4.1. A 2010 előtti és a 2022 utáni szankciórendszerek összevetése

A szakmai vitákban időnként megjelenő felvetéssel szemben a 2010 előtti PPP-szerződések is tartalmaztak kötbér- és levonási mechanizmusokat. Az ÁSZ 1118. számú jelentésének 43. oldalán (29. és 30. lábjegyzetek), valamint 51. oldalán dokumentált tényadatok rögzítik, hogy a szerződések úgynevezett hiányossági szorzókat ($K_h$) alkalmaztak: a burkolat és műtárgyak hibái, illetve a sebességkorlátozások arányos díjlevonást vontak maguk után. Az ÁSZ által ellenőrzött tíz hónapból hatban ténylegesen sor került pénzügyi levonásra a koncesszortól.

A 2022-es koncessziós rendszer újdonsága a mérési technológiák automatizálásában és a korszerű hálózati funkciók beépítésében ragadható meg. A burkolatromlást (nemzetközi egyenetlenségi index: IRI, nyomvályúmélység, felületi tapadás) folyamatosan mozgó lézeres mérőautók rögzítik, és az adatok közvetlenül beépülnek a szerződés 3/D. mellékletében rögzített kötbér- és levonási képletekbe. Emellett kötelezővé tették a burkolatvédő dinamikus tengelysúlymérő rendszerek (WIM), a teljes optikai hálózat, az intelligens forgalomirányítás (ITS), valamint az európai AFIR (Alternative Fuels Infrastructure Regulation) rendeleti keretrendszerhez illeszkedő, nagyteljesítményű e-töltőinfrastruktúra kiépítésének műszaki feltételeit és kötelezettségét.

### 4.2. Történeti és modern műszaki határérték-szabályozás

Az ÁSZ 1118. jelentés 51. oldalán rögzített történelmi rendelkezésre állási díjcsökkentési képlet:

$$
\text{RÁD}_{\text{tényleges}} = \text{RÁD}_{\text{bázis}} \times K_f \times K_h - D_{\text{egyéb}}
$$

Ahol:
* $K_f$: Fizetési fázistényező.
* $K_h$: Hiányossági tényező (üzemeltetési és burkolathibák szorzója).
* $D_{\text{egyéb}}$: Sebességkorlátozási és biztonsági dedukciók.

Ezzel szemben a 2022-es modell dinamikus műszaki határérték-szabályozása (a koncessziós szerződés műszaki-üzemeltetési mellékleteiben és a MAÚT szakmai irányelveiben rögzített indikatív szolgáltatási szintek és benchmarkok):

$$
\text{IRI} \le 1,8 \text{ mm/m}, \quad \text{Nyomvályúmélység} \le 8,0 \text{ mm}, \quad \text{SFC (tapadási tényező)} \ge 0,45
$$

A mérési szelvényen a digitális lézeres állapotfelmérést követően a szerződéses kötbér- és levonási mechanizmus szabályai szerint határérték-túllépés esetén tételes díjmegvonásra kerül sor.

---

## 5. Tőkeköltség, kockázatmegosztás és államadósság

### 5.1. A súlyozott átlagos tőkeköltség (WACC) és az állami hitelfelvétel viszonya

A projektfinanszírozási szakirodalom (EIB, EPEC) általános tapasztalata, hogy a magánprojekt kockázati prémiuma rendszerint magasabb, mint az ugyanazon szuverén kockázati környezetben elérhető állami finanszírozási költség; ez azonban nem minden konkrét konstrukcióra és nem minden finanszírozási szakaszra bizonyított automatikusan. A magánkonzorcium súlyozott átlagos tőkeköltsége (WACC) banki projekthitelekből és magasabb hozamelvárású saját tőkéből tevődik össze.

A kereskedelmi bankok a magánhitelre kockázati felárat számolnak fel, míg a konzorcium tulajdonosai a kockáztatott saját tőkéjükre piaci benchmarkként 10–14%-os elvárt belső megtérülési rátával (Equity IRR) kalkulálnak. 2021-ben, a koncesszió előkészítésekor a 10–20 éves magyar államkötvények referenciahozama 2,5–3,5% között mozgott. A magántőke bevonása tehát kilométerenként és évente finanszírozási felárat jelent a szuverén hitelfelvételhez képest, amit az elmélet szerint a magánfél hatékonyabb kivitelezési és életciklus-menedzsmentjének kellene ellensúlyoznia.

### 5.1.1. A tőkeköltség-képlet és a szuverén spread számszerű levezetése

A magánkonzorcium súlyozott átlagos tőkeköltsége (WACC) az EPEC módszertana szerint:

$$
WACC = \left( \frac{E}{V} \times r_e \right) + \left( \frac{D}{V} \times r_d \times (1 - T_c) \right)
$$

Ahol:
* **Saját tőke aránya ($E/V$):** 15–20%
* **Idegen tőke aránya ($D/V$):** 80–85% (szindikált bankhitel)
* **Elvárt saját tőke megtérülés ($r_e$):** 10–14% (a konzorcium elvárt saját tőke megtérülése; a piaci szakirodalomban szereplő Equity IRR csak indikatív proxyként, nem közvetlenül azonos fogalomként szerepel)
* **Banki hitelkamatláb ($r_d$):** Euribor/Bubor + 200–350 bázispont
* **Társasági adókulcs ($T_c$):** 9%

Indikatív számítás a 2021-es piaci környezet indikatív benchmark-feltételezéseivel:

$$
WACC_{\text{magán}} = (0,15 \times 0,12) + (0,85 \times 0,055 \times 0,91) = 0,018 + 0,0425 = \text{\textbf{6,05\%}}
$$

Ezzel szemben a szuverén kötvényhozam (ÁKK 15 éves államkötvény referenciahozam, 2021):

$$
r_g \approx \text{\textbf{2,85\%}}
$$

A finanszírozási különbözet (tőkeköltség-felár):

$$
\text{Spread} = WACC_{\text{magán}} - r_g = 6,05\% - 2,85\% = \text{\textbf{+3,20\%}} \quad \text{(320 bázispont)}
$$

*Megjegyzés:* A 3,20 százalékpontos különbség nem az MKIF tényleges szerződéses finanszírozási felára, hanem indikatív benchmark-spread a feltételezett projekt-WACC és a 2021-es szuverén hozam között.

---

### 5.2. Az ÁSZ megállapítása a mérlegen kívüliségről és a döntés-előkészítésről

Az Állami Számvevőszék 1118. számú jelentésének 39. és 40. oldala szó szerint rögzíti a 2010 előtti PPP-döntések hátterét:
> *„A Kormány döntése alapján a Közbeszerzési Eljárás feltételeit úgy kellett kialakítani, hogy a beruházás az államháztartási mérlegen kívüli tétel legyen... A VFM számítások során feltételezték, hogy a tradicionális állami beruházás mintegy 40 Mrd Ft-tal magasabb költséggel valósulna meg, amely torzította a döntést.”*

Az ÁSZ rámutatott: az állam a maastrichti adósságmutatók azonnali növekedésének elkerüléséért cserébe évtizedeken át merev, a közvetlen állami hitelnél drágább költségvetési kötelezettséget vállalt magára. Ez a megállapítás alátámasztja azt a közgazdasági kritikát, miszerint a mérlegen kívüliség fiskális illúziót teremt, ha a magasabb finanszírozási költséget nem ellensúlyozza igazolt hatékonysági többlet. A 2022-es konstrukció esetében az egyik lehetséges fiskális ösztönző a maastrichti és ESA-elszámolási hatás kezelése lehetett; ennek tényleges szerepe a 2022-es döntés-előkészítő VFM- és ESA-dokumentáció teljes ismerete nélkül nem bizonyítható ugyanolyan közvetlenül, mint a 2010 előtti PPP-k esetében.

---

### 5.3. A kockázatmegosztás szerkezete

A nemzetközi szakirodalom szerint a magántőke prémiuma akkor indokolt, ha a partner valós piaci kockázatokat vesz át az államtól. A magyar gyorsforgalmi modellekben (mind 2010 előtt, mind 2022-ben) a kockázatmegosztás aszimmetrikus képet mutat:
* **Államnál maradó kockázatok:** A rendelkezésre állási díj forgalomtól való függetlensége miatt a közvetlen forgalmi bevételkockázat döntő része az államnál marad (az állam üres sztrádák esetén is köteles a teljes díjat fizetni); a használati díjak (matrica, teherútdíj) a központi költségvetés bevételei között jelennek meg; az inflációs kockázatot az éves szerződéses indexálás révén az állam kompenzálja.
* **Koncesszor által viselt kockázatok:** A rendelkezésre állási kockázat (műszaki meghibásodás miatti sávzárások kötbérezése); a karbantartási és életciklus-kockázat (burkolatromlás helyreállítása); valamint a kivitelezési és határidő-kockázat a gyorsított 538 km felújításánál és az M1 kapacitásbővítésénél.

---

## 6. Költségvetési iskolák és makrogazdasági forgatókönyvek

### 6.1. Az egymással versengő gazdaságfilozófiák és közpénzügyi iskolák

A gyorsforgalmi koncessziós konstrukciók és a hosszú távú infrastruktúra-szervezés megítélése mögött nem pusztán politikai viták, hanem eltérő elméleti és közpénzügyi értelmezési nézőpontok feszülnek. A következő keretek nem egymást kizáró, zárt dogmatikus iskolák, hanem egymással vitatkozó közgazdasági szemléletmódok a közszolgáltatások és a magántőke viszonyáról:

1. **New Public Management és életciklus-alapú infrastruktúra-szervezés (DBFOM):**
   * *Elméleti alap:* Az állami apparátus bürokratikus, a közbeszerzési szisztéma szétaprózott (a külön tervezés, külön építés és külön fenntartás intézményi felelőtlenséget szül). Az állam hajlamos olcsó kivitelezést választani, amelynek jövőbeli felújítási számláit a mindenkori költségvetés nem tudja garantálni.
   * *A koncessziós válasz:* A Design-Build-Finance-Operate-Maintain (DBFOM) integrált életciklus-felelősség. Ha egyetlen magánvállalkozó felel a tervezésért, építésért és a 35 éves üzemeltetésért, közvetlen gazdasági érdeke fűződik a tartós műszaki megoldásokhoz, hiszen a hibák későbbi javítását és az SLA-kötbéreket neki kell állnia.
   * *Korlátok és kritikák:* A tranzakciós költségtan (Oliver Williamson, Oliver Hart) szerint a 35 éves szerződések szükségszerűen „hiányos szerződések” (incomplete contracts). Az évtizedek során felmerülő előre nem látható módosítások során a megrendelő állam függőségi helyzetbe (hold-up probléma) kerül, a magánpartner pedig monopolhelyzetét kihasználva extra járadékot érvényesíthet.

2. **Közösségi Döntések Elmélete (Public Choice School – James M. Buchanan, Gordon Tullock):**
   * *Elméleti alap:* A politikusok és bürokraták nem a tankönyvi „közjót”, hanem saját újraválasztási esélyeiket és hatalmi céljaikat maximalizáló gazdasági szereplők.
   * *A fiskális illúzió (Fiscal Illusion):* A 35 éves koncesszió a költségvetési illúzióteremtés klasszikus eszköze. Lehetővé teszi, hogy a regnáló kormányzat a politikai hasznot (átadott sztrádák, szalagátvágások, népszerűség) azonnal learatja, miközben az anyagi terheket 35 évre szétterítve a jövőbeli kormányokra és jövő generációkra terhelik át, elkerülve a népszerűtlen adóemeléseket.
   * *Járadékvadászat (Rent-seeking) és Foglyul ejtett szabályozás (Regulatory Capture):* Az állami természetes monopóliumok magánkézbe adása a belső politikai-gazdasági elit számára teremt garantált piacot és kockázatmentesített járadékot (economic rent), ahol a kockázatok az adófizetőknél maradnak, a nyereség viszont magánosítódik.

3. **Közpénzügyi és szuverén adósságelméleti nézőpont (Richard Musgrave, Arrow–Lind-tétel, Joseph Stiglitz):**
   * *Elméleti alap:* Az autópálya-hálózat stratégiai közjószág és hálózatos természetes monopólium, amelynek társadalmi haszna messze túlmutat a pénzügyi megtérülésen.
   * *Az Arrow–Lind-érvelés és a tőkeköltség-anomália:* Az Arrow–Lind-tétel közpolitikai érvelése szerint bizonyos feltételek mellett a társadalom egészére szélesen megosztott kockázat társadalmi költsége alacsonyabb lehet, mint egy koncentrált magánprojekt kockázati prémiuma; ez azonban nem azonos azzal az abszolút állítással, hogy minden állami finanszírozás tényleges piaci kamata automatikusan alacsonyabb. Ha a magánfél nem visel valós piaci (forgalmi) kockázatot, a magasabb magántőkeköltség megfizetése indokolatlan társadalmi holtteher-veszteséget jelenthet az államkötvényes finanszírozáshoz képest.
   * *A szociális diszkontráta elve:* Az államnak a jövőbeli infrastrukturális javakat nem a kereskedelmi banki profitéhséggel, hanem alacsonyabb szociális diszkontrátával kell értékelnie a jövő nemzedékek jólétének biztosítására.

4. **Statisztikai-fiskális értelmezési keret (Eurostat / ESA 2010 és Maastrichti Szabályrendszer):**
   * *Elméleti alap:* A modern PPP-k és koncessziók elterjedésének elsődleges gyakorlati mozgatórugója Európa-szerte a maastrichti adósság- és hiánykorlátok (GDP-arányos 60% adósság és 3% deficit) statisztikai kezelése.
   * *Mérlegen kívüliség (Off-balance sheet treatment):* Az Eurostat szabályrendszere lehetővé teszi, hogy ha a beruházási eszköz építési és rendelkezésre állási kockázatát a magánpartner viseli, a projekt tőkeértéke ne jelenjen meg az államháztartási hiányban és a bruttó államadósságban.
   * *Az ÁSZ 1118. számú jelentésének értékelése:* Az ÁSZ 1118. számú jelentése a vizsgált korábbi PPP-beruházások esetében dokumentálta, hogy a mérlegen kívüli elszámolás szempontja meghatározó szerepet játszott a konstrukció kiválasztásában, feláldozva a hosszú távú költségvetési rugalmasságot az azonnali statisztikai optika javításáért.

### Összehasonlító iskolamátrix: a gyorsforgalmi koncessziós modellek elméleti megítélése

| Elméleti Iskola | Fő elméleti képviselők | Alapfeltevés az államról | Tőkeköltség és finanszírozás megítélése | Kockázatallokációs fókusz | Fő veszély / Rendszerkritika |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **New Public Management (NPM)** | Williamson, Demsetz, Hart | Bürokratikus, pazarló, nem életciklus-szemléletű | A magasabb WACC-ot kompenzálja a magánszektor hatékonysága | DBFOM integráció: a kivitelező viselje a 35 éves fenntartási kockázatot | Hiányos szerződések, hold-up csapda, renegotiation járadékok |
| **Közösségi Döntések Elmélete** | Buchanan, Tullock, Niskanen | Önérdekű politikusok és bürokraták szövetsége | Fiskális illúzió: a kiadások jövőbe tolása adóemelés nélkül | Aszimmetrikus: a politikai haszon azonnali, a számla a jövő generációé | Járadékvadászat, politikai klientúraépítés, szabályozói foglyul ejtés |
| **Klasszikus Közpénzügytan** | Musgrave, Arrow, Lind, Stiglitz | Természetes monopóliumok és közjavak gondnoka | Arrow-Lind tétel: az állami finanszírozás olcsóbb, a magán-WACC holtteher-veszteség | Ha nincs keresleti kockázat a magánfélnél, a magántőke prémiuma indokolatlan | Drága magánfinanszírozás, indokolatlan tőkejáradék az adófizetők kárára |
| **Statisztikai-Fiskális Iskola** | Eurostat, ESA 2010 szabályozók | Maastrichti adósság- és hiánystatisztikák rabja | Nem gazdasági, hanem könyvelési optimumra törekszik | Formális kockázatátadás az off-balance sheet státusz eléréséhez | Évtizedes költségvetési merevség a pillanatnyi adósságoptikáért cserébe |

---

### 6.2. Mikor melyik fél számára kedvezőbb a konstrukció?

A szerződéses feltételek dinamikája eltérő makrogazdasági pályákon más-más félnek kedvez:

* **Mikor előnyösebb az államnak?**
  * *Dinamikus forgalomnövekedés idején:* A használatarányos teherútdíj-bevételek (HU-GO) az államhoz folynak be, miközben a nagyobb igénybevétel miatti burkolatjavítás költségeit a szerződéses SLA szerint a koncesszornak kell fedeznie.
  * *Költségvetési restrikció és szigorú hitelkorlát idején:* Amikor az állami beruházások leállnak, a szindikált magánhitelek fenntartják az infrastrukturális felújításokat.
  * *Költségvetési forráskivonás megakadályozásakor:* Az állam nem tudja elvonni a fenntartási forrásokat, garantálva a műszaki állapot szinten tartását.

* **Mikor előnyösebb a koncesszornak?**
  * *Magas inflációs környezetben:* Az inflációkövető indexálás azonnal megemeli a díjbevételt, miközben a fix tőketartozások és hosszú távú beszállítói szerződések lassabban drágulnak.
  * *Gazdasági visszaesés és forgalomcsökkenés idején:* A forgalomtól független rendelkezésre állási díj biztosított marad, miközben a csökkenő járműforgalom mérsékli a pályatest kopását.
  * *A jó állapotú 700 km-es hálózaton:* Ahol nincs szükség azonnali mélyfelújításra, a rutinüzemeltetés mellett jelentős működési eredmény realizálható.
  * *Hozamcsökkenési környezetben:* A korábban felvett bankhitelek olcsóbbra refinanszírozhatók, ami refinanszírozási nyereséget eredményez.

---

## 7. Jogállamiság, bírósági ítéletek és a transzparencia kötelezettsége

A gyorsforgalmi koncessziós szerződés pénzügyi mellékleteinek megismerhetősége kapcsán lefolytatott bírósági eljárások alapvető jelentőségűek a közpénzek átláthatósága szempontjából. A peres eljárás és a legfelsőbb bírói fórumok döntései világos precedenst teremtettek:

1. **A bírósági eljárási lánc:**
   * A felperes (Wiedemann Tamás újságíró) közérdekű adat kiadása iránt pert indított a Nemzeti Koncessziós Iroda (NKOI) ellen, amelybe a nyertes koncesszor (MKIF Zrt.) az alperes érdekében beavatkozóként lépett be.
   * A megismételt elsőfokú eljárásban a Fővárosi Törvényszék `25.P.21.778/2023/18.` számú kijavított ítéletével elrendelte a szerződés 11 mellékletének kiadását, elutasítva az MKIF szakértői bizonyítási indítványát.
   * A Fővárosi Ítélőtábla **`2.Pf.20.469/2023/9/I.`** számú jogerős ítéletével az elsőfokú döntést megváltoztatta, és kötelezte az NKOI-t, hogy a 3/E. és a 15. számú mellékletet (az Ajánlat II. kötet 120–179. oldalain lévő díjszámítási táblázatokat) **kitakarás nélkül adja ki**.
2. **A Kúria `Pfv.IV.21.194/2023/15.` számú felülvizsgálati ítélete (2024. március 13., `K-PJ-2024-94`):**
   * A Kúria a másodfokú jogerős ítéletet **hatályában fenntartotta**.
   * A Kúria elvi éllel mondta ki: az üzleti titok védelme és a közpénzek nyilvánossága közötti mérlegelés (Infotv. 27. § (3) bek.) **jogkérdés**, amely a bíróság feladata, így nem igényel minden esetben igazságügyi szakértői bizonyítást.
   * Rögzítette az **adatelv** elsőbbségét az iratelvvel szemben: teljes dokumentumok és szerződéses mellékletek nem zárhatók el a nyilvánosság elől automatikusan.
3. **Az Alkotmánybíróság `3372/2024. (X. 8.) AB végzése` (`IV/1946/2024`):**
   * Az Alkotmánybíróság az MKIF Zrt. beavatkozó által benyújtott 18 oldalas alkotmányjogi panaszt végzésével **visszautasította**, így a Kúria jogerős döntése hatályban maradt.
4. **Kapcsolódó elvi döntések és a jogi mérlegelés természete:**
   * A bíróságok döntései alapján az adatkezelő nem zárhatja el automatikusan a közpénzekkel kapcsolatos szerződéses adatokat az üzleti titokra való absztrakt hivatkozással; a korlátozást konkrét adatonként, bizonyított aránytalan piaci sérelemre és szigorú bírói arányossági mérlegelésre (közérdekűségi teszt) kell alapítani. A verseny tisztaságára való hivatkozás a közbeszerzési eljárás lezárását követően már nem indokolja a közfeladat ellátására fordított közpénzek titkosítását (lásd kapcsolódó precedensként: Kúria `Pfv.IV.21.124/2023/16.`). Ez az elvi joggyakorlat megerősíti a közpénzek nyilvánosságának elsőbbségét, ugyanakkor rögzíti, hogy a nyilvánosság korlátozása csak egyedi, igazolt jogsérelem alapján merülhet fel.

---

## 8. Összegzés: a szakmai elemzés főbb következtetései

A primer dokumentumok, számvevőszéki jelentések, nyilvános bírósági döntések és indikatív pénzügyi modellek alapján a következő szakmai kép rajzolódik ki.

### 1. Költségvetési cash flow

Az ismert éves keretből visszaszámított, mintegy 525 millió Ft/km/év indikatív MKIF-átlag az alkalmazott indexálási módszertől függően körülbelül 6–16%-kal alacsonyabb vagy azonos nagyságrendű lehet, mint a 2010 előtti M6-díj mai értéke. Ez azonban nem bizonyítja, hogy az MKIF-konstrukció teljes életciklus-költsége vagy társadalmi költsége is alacsonyabb.

A közvetlen euróalapú árfolyamkitettség a korábbi konstrukcióhoz képest mérséklődik vagy megszűnik, miközben a szerződéses díjindexálás és a makrogazdasági költségkockázatok jelentős része továbbra is az államot terheli. Az 525 millió Ft/km/év nem a szerződésből közvetlenül kiolvasott homogén alapdíj, hanem az ismert éves keretből és az 1237 km-es induló hálózatból visszaszámított indikatív átlag.

### 2. Vagyoni és műszaki tartalom

A korábbi M6/M60-PPP-k magasabb fajlagos díja mögött jelentős zöldmezős beruházás, alagút- és műtárgyépítés, valamint teljes nyomvonal-kialakítás állt. A 2022-es modellben az 1237 km-es induló hálózat döntő többsége már korábban, vegyes finanszírozási forrásokból megépült, ezért a koncessziós díj nem egy teljes egészében új hálózat létrehozásának tőkeköltségét tükrözi.

A jelenlegi modell fő feladata az üzemeltetés, a gyorsított szintrehozás, a szerződéses életciklus-fenntartási kötelezettségek teljesítése és a forgalom alatti kapacitásbővítés. A két modell fajlagos díjai ezért csak a műszaki tartalom, az időérték, az indexálás és a kockázatmegosztás együttes figyelembevételével hasonlíthatók össze.

### 3. Finanszírozás és kockázatmegosztás

A rendelkezésre állási díj forgalomtól való függetlensége miatt a közvetlen keresleti kockázat jelentős része az államnál marad, miközben a koncesszor építési, fenntartási, rendelkezésre állási és életciklus-kockázatokat visel. A magántőke indikatív WACC-felára csak akkor igazolható közpénzügyileg, ha ezt mérhető kivitelezési, üzemeltetési és életciklus-hatékonyság ellensúlyozza.

A 2022-es modell ezért nem tekinthető automatikusan a korábbi PPP-k ellentétének: a műszaki feladatok és a kedvezményezett tulajdonosi kör megváltoztak, miközben a hosszú távú állami fizetési kötelezettség, a magántőke-finanszírozás és a részleges állami kockázatviselés alaplogikája fennmaradt.

A nyilvánosságra került cég- és sajtóadatok szerint a koncessziós konzorcium magántőkealapjai Mészáros Lőrinchez és Szíjj Lászlóhoz köthető gazdasági érdekeltségekhez kapcsolódnak[^5]. Ez a tulajdonosi háttér önmagában nem bizonyít jogellenességet, túlzott árazást vagy tényleges extraprofitot; közpolitikai szempontból azonban lényeges, mert megmutatja, kikhez kapcsolódhatnak a több évtizedes állami pénzáramokból származó hozamok.

### 4. Transzparencia

A Kúria konkrét szerződéses mellékletek kiadásával kapcsolatos felülvizsgálati ítélete és az Alkotmánybíróság panaszt visszautasító végzése megerősíti, hogy a közpénzekkel kapcsolatos szerződéses adatok nem zárhatók el automatikusan üzleti titokra hivatkozva. A nyilvánosság korlátozását konkrét adatokhoz, bizonyított piaci sérelemhez és arányossági mérlegeléshez kell kötni. Ez azonban nem jelenti azt, hogy minden szerződéses adat minden körülmények között korlátozás nélkül nyilvános.

## Végső közpolitikai következtetés

A közpolitikai törésvonal nem egyszerűen a külföldi és magyar tulajdon között húzódik. A döntő kérdés az, hogy a koncesszió ugyanazt a közszolgáltatást milyen teljes életciklus-költség mellett biztosítja, ki viseli ténylegesen a keresleti, inflációs és finanszírozási kockázatokat, valamint ki részesedik a több évtizedes állami pénzáramokból.

A 2022-es modell hazai tulajdonosi háttere önmagában nem jelent közpénzügyi előnyt. A tulajdonosváltás csak akkor jelentene valódi reformot, ha mérhető kockázatátadással, átlátható és versenyeztetett árazással, valamint igazolt Value for Money eredménnyel járna.

**A jelenlegi bizonyítékok alapján a 2022-es MKIF-konstrukció nem bizonyított közpénzügyi paradigmaváltás, hanem eltérő műszaki tartalmú és eltérő kedvezményezetti körű koncessziós folytatás.** A korábbi PPP-khez képest bizonyos fajlagos cash-flow-mutatókban akár kedvezőbbnek is tűnhet, de ez nem bizonyítja a teljes életciklus-költség alacsonyabb voltát. A lényegi változás ezért nem az, hogy a koncessziós logika megszűnt volna, hanem az, hogy a hosszú távú állami pénzáramokhoz kapcsolódó kedvezményezetti kör megváltozott.

---

## Források és lábjegyzetek

[^1]: **Bírósági határozatok:** Kúria *Pfv.IV.21.194/2023/15.* sz. ítélete (dátum: 2024. március 13., azonosító: `K-PJ-2024-94`); Fővárosi Ítélőtábla *2.Pf.20.469/2023/9/I.* sz. jogerős ítélete; Fővárosi Törvényszék *25.P.21.778/2023/18.* sz. ítélete az MKIF gyorsforgalmi úthálózat-koncessziós szerződés 11 pénzügyi mellékletének kiadásáról; valamint Alkotmánybíróság *3372/2024. (X. 8.) AB végzése* (`IV/1946/2024`). Kapcsolódó elvi döntésként: Kúria *Pfv.IV.21.124/2023/16.* (MOL hulladékgazdálkodás).

[^2]: **Állami Számvevőszék:** *Jelentés a 2009–2010-ben befejeződő autópálya beruházások és pénzügyi folyamatai ellenőrzéséről.* 1118. sz. jelentés, Budapest, 2011. július (különösen: 39–55. o.); *Jelentés a gyorsforgalmi úthálózattal kapcsolatban állami feladatot ellátó szervezetrendszer működésének ellenőrzéséről.* 1003. sz. jelentés, Budapest, 2010. Központi Statisztikai Hivatal (KSH): *STADAT 1.1.1.2. Fogyasztóiár-indexek*, valamint *STADAT 1.1.1.32. Építményfajták termelői árindexei (Utak, autópályák 2010–2025)*.

[^3]: **Magyar Közút Nonprofit Zrt.:** *2020. és 2021. évi könyvvizsgált Éves Beszámolói, Mérlegei és Eredménykimutatásai.* A társaság éves nettó árbevétele és költségvetési támogatása 2021-ben 386,1 milliárd Ft-ot tett ki. MKIF Zrt. hivatalos adatközlései a szintrehozási programról (2022–2024).

[^4]: **European PPP Expertise Centre (EPEC) / European Investment Bank (EIB):** *Value for Money Assessment – Review of approaches and key issues.* EIB, Luxembourg, 2015, pp. 22–32; HM Treasury: *The Green Book: Central Government Guidance on Appraisal and Evaluation.* UK Government, London, 2020; Voszka Éva: *Államosítás, privatizáció, államosítás.* Közgazdasági Szemle, LX. évf., 2013; Major Iván: *A korlátozó szabályozástól az ösztönző szabályozásig.* Közgazdasági Szemle, LI. évf., 2004.

[^5]: **Tulajdonosi és érdekeltségi háttér forrásai:** A koncessziós eljárásban nyertes konzorcium magántőkealap-struktúrája és alapkezelői háttere: 444.hu feltáró elemzése (*Már milliárdos osztalékhoz jutottak Mészárosék az autópálya-koncesszión*, 2024. május 31.); G7.hu gazdasági elemzései a gyorsforgalmi koncessziós magántőkealapok struktúrájáról (a konzorciumot alkotó hét magántőkealap: Themis, Konzum PE, Opus Bridge, Via M1, Via M3, Via M5, Via M7; az alapok kezelői és kapcsolt vállalkozásai a nyilvános cégbírósági adatok szerint Mészáros Lőrinc és Szíjj László gazdasági érdekeltségeihez kapcsolódnak).
