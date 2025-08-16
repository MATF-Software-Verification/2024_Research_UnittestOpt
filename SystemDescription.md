# Istraživački projekat iz oblasti verifikacije softvera
### Tema: Optimizacija jediničnih testova koriscenjem nedeterminističkih algoritama i algoritama veštačke inteligencije
### Autor: Dušan Pantelić 1062/2024

## Opis problema:
Jedinični testovi su ključni za osiguranje kvaliteta softvera, ali njihovo izvršavanje može biti vremenski zahtevno i resursno intenzivno.
Optimizacija jediničnih testova može značajno poboljšati efikasnost procesa testiranja, smanjujući vreme potrebno za izvršavanje testova i resurse koji se koriste.
U opštem slučaju pronalaženje optimalnog podskupa testova je NP-težak problem, što znači da ne postoji poznati polinomijalni algoritam koji može efikasno rešiti ovaj problem za sve moguće ulaze.

## Opis rešenja problema:
U cilju optimizacije procesa testiranja, istražujemo primenu nedeterminističkih algoritama i veštačke inteligencije za određivanje optimalnih ili blizu optimalnih podskupova testova koji se izvršavaju, a da se pritom očuva pokrivenost koda i efikasnost u željenoj meri ukoliko je to moguće.
Ovim pristupom se žrtvuje zagarantovanost pronalaženja optimalnog rešenja u korist bržeg i efikasnijeg procesa optimizacije, što je često prihvatljivo u praksi. U nastavku su opisani ključni aspekti rešenja:

### Informacije o podskupu testova:
Kako je izvršavanje testova uglavnom vremenski zahtevno (zbog čega i vršimo optimizaciju), samo inicijalno izvršavamo testove i čuvamo potrebne informacije poput pokrivenosti i vremena izvršavanja.
Kasnije kada su nam potrebne informacije o podskupu testova to preračunavamo na osnovu inicijalnih podataki čime u velikoj meri optimizujemo vremensku zahtevnost rešenja.


### Funkcija cilja optimizacije:
Funkcija cilja optimizacije evaluira razmatrani podskup, i definisana je kao linearna kombinacija tri faktora:
1. **Pokrivenost**: Procenat koda koji je pokriven podskupom.
2. **Smanjenje broja testova**: Procenat smanjenja broja testova u odnosu na originalni skup testova.
3. **Efikasnost**: Procenat smanjenja vremena izvršavanja testova u odnosu na originalni skup testova.

### Ograničenje optimizacije:
Postoji moguće ograničenje optimizacije koje se odnosi na minimalnu pokrivenost koda koju treba postići prilikom optimizacije, izraženo kao procenat.
Ovo ograničenje osigurava da optimizovani podskup testova i dalje pokriva značajan deo koda.


### Korišćeni algoritmi:
1. **Genetski algoritam**: Koristi evolucione principe kao što su selekcija, ukrštanje i mutacija za generisanje novih podskupova testova.
Početna populacija se sastoji od nasumično generisanih jedinki (podskupa testova), koje su su predstavljene nizom bitova dužine jednake veličini inicijalnog skupa testova i predstavljaju indikator da li konkretni test slučaj ulazi u podskup.
Tokom sledećih iteracija tj. generacija nove jedinke nastaju od jedinki iz prethodne generacije ukrštanjem, gde od dva roditelja nastaju dva deteta, pri čemu se indikator konkretnog test slučaja uzima na nasumičan nacin od jednog od roditelja kod prvog deteta, a drugo dete će uzeti indikator roditelja koji nije bio izabran.
Izbor roditelja za ukrštanje se vrši nasumično gde jedna jedinka moze biti izabrana više puta.
Funkcija cilja se koristi za ocenu kvaliteta jedinke (podskupa testova) i vodi optimizaciju ka boljem rešenju kroz više generacija. 
Radi odrzavanja raznolikosti i stabilnosti rešenja, koristi se mutacija i elitizam, čime se osigurava da najbolja rešenja ostanu u populaciji, ali i da se spreci zaglavljivanje u lokalnom optimumu.
Algoritam se zaustavlja nakon broja iteracija definisanog u parametrima.
2. **Bajesovska optimizacija**: Koristi Bajesovsko zaključivanje za optimizaciju pomoću Optuna biblioteke, omogućavajući efikasno istraživanje prostora rešenja. 
Uglavnom se koristi kada je potrebno brzo generisati rešenja bez potrebe za velikim brojem iteracija (obično je evaluacija rešenja skupa kao npr. izvršavanje testova).
Incijalno se moze zadati početni podskup testova koji se koristi kao početna tačka za optimizaciju, ali i odredjeni broj nasumičnih rešenja koje služe za inicijalnu pretragu prostora rešenja.
Na osnovu prethodnih rešenja, Bajesovska optimizacija koristi probabilistički model da predvidi koje kombinacije testova mogu dati bolje rezultate, čime se fokusira na istraživanje najperspektivnijih delova prostora rešenja.
Algoritam se zasniva na principu iterativnog ažuriranja trenutnog rešenja na osnovu rezultata prethodnih evaluacija, čime se smanjuje broj potrebnih evaluacija i ubrzava proces optimizacije.
Algoritam se zaustavlja nakon broja iteracija definisanog u parametrima.
3. **Algoritam slučajne pretrage**: Izvodi slučajnu pretragu podskupa testova koji održava trenutno optimalno rešenje, omogućavajući brzo generisanje rešenja bez potrebe za kompleksnim algoritmima.
Verovatnoća uključivanja test slučaja je parametrizovana, tako da ako smatramo da je optimalni podskup gust u odnosu na inicijani skup (mali broj testova treba izbaciti), tada koristimo veliku verovatnoću uključivanja i obratno.
4. **Brute-force algoritam**: Pretražuje sve moguće kombinacije testova i bira najbolju kombinaciju koja zadovoljava uslove pokrivenosti i efikasnosti.
Vremenski moze biti vrlo zahtevan, ali garantuje pronalaženje optimalnog rešenja. Algoritam se zaustavlja nakon broja iteracija definisanog u parametrima.
U projektu ga koristimo samo za testiranje i proveru ispravnosti ostalih algoritama, jer je veoma spor i neefikasan za veće skupove testova.

## Opis arhitekture sistema:
Sistem je razvijen u Python programskom jeziku i koristi sledeće biblioteke:
- `unittest`, `pytest`, `doctest`: Za pisanje i izvršavanje jediničnih testova.
- `coverage`: Za merenje pokrivenosti koda testovima.
- `optuna`: Za implementaciju Bajesovske optimizacije.
- `numpy`, `pandas`: Za obradu podataka i numeričke operacije.
- `customtkinter`: Za izradu grafičkog korisničkog interfejsa (GUI) koji omogućava korisnicima da interaguju sa sistemom.

### Glavne komponente sistema:
#### 1. **Manipulacija pokrivenošću koda (src/coverage)**
Ova komponenta se bavi prikupljanjem svih test slučajeva u nekom projektu, njihovim izvršavanjem i prikupljanjem metapodataka o pokrivenosti koda,
ali i preračunavanjem metapodatako o pokrivenosti koda za zadati podskup testova na osnovu inicijalnih testova i njihovih metapodatako bez ponovnog izvršavanja.

- **Model Podataka o Pokrivenosti (coverage_data.py)**: Definiše strukturu podataka koja sadrži informacije o pokrivenosti koda,
uključujući linije koda koje su pokrivene testovima, vreme izvršavanja i status testova.
- **Obrazac Rukovanja Pokrivenošću (coverage_data_handler.py)**: Definiše apstraktnu klasu koja pruža interfejs za rukovanje podacima o pokrivenosti koda. 
- **Konkretni Rukovodilac Pokrivenošću (npr. python_coverage_data_handler.py)**: Implementira abstraktne metode definisane u obrascu specifične za konkretni programski jezik (trenutno podržan jezik Python).

#### 2. **Optimizacija testova (src/optimization)**
Ova komponenta sadrži implementaciju različitih algoritama za optimizaciju testova, uključujući genetski algoritam, Bajesovsku optimizaciju, slučajnu pretragu i brute-force algoritam.
- **Obrazac Optimizacije (base_optimisation.py )**: Definiše apstraktnu klasu koja pruža interfejs za implemetaciju algoritama za optimizaciju.
- **Konkretni Optimizatori (algorithms/*)**: Implementiraju abstraktne metode definisane u obrascu specifične za konkretni optimizacioni algoritam. 
Svi gore navedeni algoritmi su implementirani kao konkretni optimizatori.
- **Konfiguracija Optimizacije (configs/*)**: Definiše strukturu podataka koja sadrži konfiguraciju optimizacije specifičnu za konkretni algoritam.
- **Menadžer Optimizacije (optimisation.py)**: Upravlja optimizacijom testova, uključujući pokretanje  izabrane optimizacije za učitan projekat, čuvanje rezultata i upravljanje genralnom konfiguracijom optimizacije.
- **Izveštaj o Optimizaciji (optimisation_report.py)**: Definiše strukturu podataka koja sadrži rezultate optimizacije, uključujući pokrivenost, vreme izvršavanja i broj testova u optimizovanom skupu, kao i metapodatke o konfiguraciji i projektu.

#### 3. **Menadžer Projekta (src/project/target_project.py)**
Ova komponenta se bavi učitavanjem, validacijom i upravljanjem projektima koji sadrže jedinične testove.

#### 4. **Korisnički interfejs (src/gui)**
Ova komponenta implementira grafički korisnički interfejs (GUI) koji omogućava korisnicima da interaguju sa sistemom, učitavaju projekte, konfigurišu optimizaciju i pokreću optimizaciju testova.
- **Specijalizovani segmenti**: 
  - **Project Loader**: Omogućava korisnicima da učitaju projekte koji sadrže jedinične testove.
  - **Project Info**: Prikazuje informacije o učitanom projektu, uključujući putanju, broj testova, pokrivenost i vreme izvršavanja.
  - **Optimization Settings**: Omogućava korisnicima da konfigurišu parametre optimizacije, uključujući važnost pokrivenosti, smanjenja broja testova i efikasnosti.
  - **Algorithm Settings**: Prikazuje specifične opcije za konfiguraciju izabranog optimizacionog algoritma.
  - **Optimization Controller**: Kontroliše pokretanje optimizacije i prikaz rezultata.
  - **Export**: Omogućava korisnicima da sačuvaju rezultate optimizacije u JSON formatu.
- **Upravljanje procesima**: Proces učitavanja projekta i optimizacije testova se odvija u pozadini, omogućavajući korisničkom interfejsu da ostane responzivan tokom dugotrajnih operacija.


### Protok podataka:
- **Učitavanje projekta**:
  - Korisnik bira projekat koji sadrži jedinične testove.
  - Sistem učitava testove i prikuplja metapodatke o pokrivenosti koda i vremenu izvršavanja.
  - Projekat se validira, tj. proverava se da li sadrži podržane jedinične testove.
  - Inicijalne informacije o projektu se prikazuju.
- **Konfiguracija optimizacije**:
  - Korisnik podešava parametre optimizacije i bira optimizacioni algoritam i konfiguriše njegove specifične parametre.
- **Optimizacija**:
  - Korisnik pokreće optimizaciju.
  - Sistem izvršava izabrani optimizacioni algoritam na osnovu konfiguracije i inicijalnih metapodataka o pokrivenosti koda.
- **Obrada rezultata**:
  - Rezultati optimizacije se prikupljaju i prikazuju korisniku.
  - Korisnik može sačuvati rezultate optimizacije u JSON formatu.

## Prostor za unapređenje:
1. **Podrška za više jezika**:
Trenutno je podržan samo Python, ali se može proširiti na druge programske jezike kao što su Java, C++, JavaScript itd. 
To bi zahtevalo implementaciju novih konkretnih rukovodilaca pokrivenošću specifičnih za te jezike unutar `coverage` modula.
2. **Dodatni algoritmi optimizacije**:
Mogu se dodati novi algoritmi optimizacije unutar `optimization/algorithms` modula, kao što su algoritmi zasnovani na mašinskom učenju ili heuristički algoritmi.
3. **Poboljšanje korisničkog interfejsa**:
GUI se može unaprediti dodavanjem novih funkcionalnosti, kao što su vizualizacija rezultata optimizacije, napredne opcije filtriranja testova i slično.