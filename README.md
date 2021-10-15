# Laboratoarele 5, 6 și 7 - Săptămânile 5, 6 și 7

Fiecare student își calculează problema asignată astfel: `1 + cod % 4`, unde `cod` este codul vostru din lista de note - cereți codul cadrului didactic de la laborator dacă nu îl știți deja. De exemplu, pentru codul `1235` problema asginată este `1 + 1235 % 4 = 1 + 3 = 4`.

Toate problemele trebuie să aibă un meniu și o posibilitate de a vizualiza toate datele existente (show all).

Trebuie să respectați organizarea codului prezentată la curs și seminar, adică să aveți cel puțin următoarele pachete și fișiere:
```
- Domain
  - Modul pentru entitatea din problema voastră, cu getteri etc.
- Logic
  - Module pentru calcule
- UserInterface
  - Module pentru interfața cu utilizatorul
- Tests
  - Module pentru teste
```

Trebuie predate:
1. Minim o funcționalitate în prima săptămână, minim încă două în a doua săptămână și toate în a treia săptămână.

2. Alte cerințe comunicate în cadrul laboratoarelor, seminarelor sau cursului. 

3. Bonus `5p`: 
- Folosiți github issues pentru a marca iterațiile (milestones), funcționalitățile și task-urile (activitățile).
- Bonusurile se acordă ca note peste `10`, doar dacă iterația este de nota `10`. De exemplu, puteți obține toate punctele bonus primind notele `12`, `12`, `11` în cele trei săptămâni alocate temei. Nu puteți primi mai mult de `2` puncte bonus într-o săptămână.

4. Bonus `10p`:
- Folosiți un sistem mai avansat care permite organizarea mai clară a iterațiilor, funcționalităților și activităților. De exemplu: Asana, dar pot fi și altele.
- Bonusurile se acordă ca note peste `10`, doar dacă iterația este de nota `10`. De exemplu, puteți obține toate punctele bonus primind notele `13`, `14`, `13` în cele trei săptămâni alocate temei. Nu puteți primi mai mult de `4` puncte bonus într-o săptămână.

Temele se predau exclusiv într-un IDE (PyCharm, VS Code etc.).

--

1. Scrieți un program pentru gestionarea unei asociații de proprietari. Vor fi suportate operațiile:  
   1.1. Adăugare / ștergere / modificare cheltuială: se efectuează pe bază de număr de apartament. O cheltuială conține număr apartament, suma, data (`DD.MM.YYYY`) și tipul: `întreținere`, `canal`, `alte cheltuieli`.  
   1.2. Ștergerea tuturor cheltuielilor pentru un apartament dat.  
   1.3. Adunarea unei valori la toate cheltuielile dintr-o dată citită.  
   1.4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.  
   1.5. Ordonarea cheltuielilor descrescător după sumă.  
   1.6. Afișarea sumelor lunare pentru fiecare apartament.  
   1.7. Undo.  

2. Scrieți un program pentru gestionarea unui inventar dintr-o instituție. Vor fi suportate operațiile:  
   2.1. Adăugare / ștergere / modificare obiect: se efectuează pe bază de număr de inventar / ID. Un obiect conține: ID, nume, descriere (nenule), preț achiziție, locație (exact `4` caractere).  
   2.2. Mutarea tuturor obiectelor dintr-o locație în alta.  
   2.3.	Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.  
   2.4.	Determinarea celui mai mare preț pentru fiecare locație.  
   2.5.	Ordonarea obiectelor crescător după prețul de achiziție.  
   2.6.	Afișarea sumelor prețurilor pentru fiecare locație.  
   2.7.	Undo.  

3. Scrieți un program pentru gestionarea rezervărilor unei companii aeriene. Vor fi suportate operațiile:  
   3.1. Adăugare / ștergere / modificare rezervare: se efectuează pe bază de număr de rezervare / ID. O rezervare conține: ID, nume, clasa (`economy`, `economy plus`, `business`), preț, checkin făcut (`da` / `nu`).  
   3.2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.  
   3.3. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.   
   3.4. Determinarea prețului maxim pentru fiecare clasă.  
   3.5. Ordonarea rezervărilor descrescător după preț.  
   3.6. Afișarea sumelor prețurilor pentru fiecare nume.  
   3.7. Undo.  

4. Scrieți un program pentru gestionarea unei librării. Vor fi suportate operațiile:  
   4.1. Adăugare / ștergere / modificare vânzare: se efectuează pe bază de număr de vânzare / ID. O vânzare conține: ID, titlu carte, gen carte, preț, tip reducere client (`none`, `silver`, `gold`).  
   4.2. Aplicarea unui discount de `5%` pentru toate reducerile silver și `10%` pentru toate reducerile gold.  
   4.3. Modificarea genului pentru un titlu dat.  
   4.4. Determinarea prețului minim pentru fiecare gen.  
   4.5. Ordonarea vânzărilor crescător după preț.  
   4.6. Afișarea numărului de titluri distincte pentru fiecare gen.  
   4.7. Undo.  
