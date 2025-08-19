# Istraživački projekat iz oblasti verifikacije softvera
### Tema: Optimizacija jediničnih testova koriscenjem nedeterminističkih algoritama i algoritama veštačke inteligencije
### Autor: Dušan Pantelić 1062/2024

## Uputstvo za pokretanje
### 1. Kloniranje repozitorijuma
```bash 
  git clone https://github.com/MATF-Software-Verification/2024_Research_UnittestOpt.git
```

### 2.  Instalacija potrebnih biblioteka
```bash 
  cd ./2024_Research_UnittestOpt
  pip install -r requirements.txt
```

### 3. Pokretanje programa
```bash
  python unittest_opt.py
```

### 4. Pokretanje testova
```bash
  pytest tests/ -v
```

### 5. Korišćenje primera realnog projekta
Unutar foldera `data-example_project` nalazi se kompresovani primer realnog projekta koji sadrži jedinične testove.
Projektaj je potrebno raspakovati u željenu lokaciju, a zatim instalirati potrebne biblioteke unutar njega. 
```bash
  cd 'PROJECT_PATH'
  pip install -e .
```
Nakon instalacije biblioteka, projekat je spreman za korišćenje i može se učitati u aplikaciju klikom na dugme **Load Project** unutar sekcije **Project Loader**.


## Upustvo za korišćenje
### 1. Pokretanje programa
```bash
  python unittest_opt.py
```
### 2. Učitavanje projekta koji sadrži jedinične testove
Klikom na dugme **Load Project** unutar sekcije **Project Loader** učitavaju se jedinični testovi iz selektovanog projekta/foldera. Ovaj projekat/folder treba da sadrži jedinične testove napisane u okviru `unittest` ili `pytest` biblioteke. Nakon selektovanja projekta, pronalaze se i pokreću svi testovi u njemu i sakupljaju se metapodaci o izvršenim testovima kao što su nazivi, broj, pokrivenost i vreme izvršavanja testova.

### 3. Informacije o učitanom projektu
Kada se učita projekat, unutar sekcije **Project Info** prikazuju se informacije o njemu:
1. Putanja do projekta
2. Ukupan broj testova u projektu
3. Ukupana pokrivenost testova
4. Ukupno vreme izvršavanja testova

### 4. Konfiguracija optimizacije
Unutar sekcije **Optimization Settings** moguće je izabrati željeni algoritam i konfigurisati parametre optimizacije:
1. **Coverage Importance**: Stepen važnosti pokrivenosti testova prilikom optimizacije. Vrednost može biti između 0 i 1, gde 0 znači da pokrivenost nije važna, a 1 da je veoma važna.
2. **Reduction Importance**: Stepen važnosti smanjenja broja testova prilikom optimizacije. Vrednost može biti između 0 i 1, gde 0 znači da smanjenje broja testova nije važno, a 1 da je veoma važno.
3. **Efficiency Importance**: Stepen važnosti efikasnosti vremena izvršavanja testova prilikom optimizacije. Vrednost može biti između 0 i 1, gde 0 znači da efikasnost nije važna, a 1 da je veoma važna.
4. **Minimal Coverage**: Minimalna pokrivenost koju treba postići prilikom optimizacije. Vrednost može biti između 0 i 1, ako se na osnovu prethodnih parametara dobije podskup testova koji narušava minimalnu pokrivenost testova, taj podskup se odbacuje i optimizacija se ponavlja.
5. **Algorithm**: Izbor algoritma koji će se koristiti za optimizaciju testova. Dostupni su:
   - **Genetic Optimisation**: Algoritam koji koristi evolucione principe za optimizaciju.
   - **Bayesian Optimisation**: Algoritam koji koristi Bajesovsko zaključivanje za optimizaciju pomoću Optuna biblioteke.
   - **Random Optimisation**: Algoritam slucajne pretrage podskupa testova koji odrzava trenutno optimalno rešenje.
   - **Bruteforce Optimisation**: Algoritam koji pretražuje sve moguće kombinacije testova i bira najbolju.

### 5. Konfiguracija optimizacionog algoritma
U zavisnosti od prethodno izabranog algoritma optimizacije u sekciji **{Algorithm_Name} Settings** prikazuju se dodatne opcije za konfiguraciju konkretnog optimizacionog algoritma:
   - **Genetic Optimisation Settings**:
     - **Number of Iterations**: Broj generacija koje će algoritam proći tokom optimizacije.
     - **Population Size**: Broj jedinki u populaciji tokom optimizacije.
     - **Mutation Factor**: Verovatnoća mutacije jedinke u populaciji, što utiče na raznolikost rešenja.
     - **Elitism Factor**: Procenat najboljih jedinki koje se prenose u sledeću generaciju bez mutacije, čime se osigurava očuvanje kvalitetnih rešenja.
     - **Random Seed**: Seme za generisanje slučajnih brojeva, što omogućava reproduktivnost rezultata optimizacije.
   - **Bayesian Optimisation Settings**:
     - **Number of Trials**: Broj pokušaja optimizacije koje će algoritam izvršiti.
     - **Random Seed**: Seme za generisanje slučajnih brojeva, što omogućava reproduktivnost rezultata optimizacije.
   - **Random Optimisation Settings**: 
        - **Number of Trials**: Broj pokušaja optimizacije koje će algoritam izvršiti.
        - **Test Inclusion Probability**: Verovatnoća uključivanja testa u optimizovani skup testova. Ako zelimo random podskup sa mnogo ukljucenih testova povecavamo verovatnocu u suprotnom smanjujemo.
        - **Random Seed**: Seme za generisanje slučajnih brojeva, što omogućava reproduktivnost rezultata optimizacije.
   - **Bruteforce Optimisation Settings**: Nema dodatnih opcija, jer algoritam pretražuje sve moguće kombinacije testova.

### 6. Pokretanje optimizacije
Unutar sekcije **Optimization Controller** klikom na dugme **Start Optimization** pokreće se optimizacija testova prema izabranim parametrima.

### 7. Prikaz rezultata optimizacije
Unutar sekcije **Optimization Report** prikazuju se detalji optimizacije kao i rezultati optimizacije.

### 8. Izvoz rezultata optimizacije
Klikom na dugme **Export** unutar sekcije **Export Optimization Report** detalji i rezultati optimizacije se izvoze u JSON fajl na izabranoj lokaciji.
