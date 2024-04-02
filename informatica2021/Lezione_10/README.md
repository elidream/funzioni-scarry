# Laboratorio di informatica (10/12)
### Prof. Stefano Carrazza - Corso C - 2021/22

**Riassunto:** Esercizi di base in C++: filtering e plotting.

Prima di iniziare suggeriamo di create una cartella per questa lezione in cui potete salvare tutti i files che saranno creati per gli esercizi.
```bash
cd ~/           # ci porta alla home directory
mkdir lezione10  # crea la directory sulla vostra home
cd lezione10     # entrate dentro la cartella
```
dopodiché creare un `makefile` con le istruzioni di compilazione per tutti gli esercizi.

## Esercizio 1 - Data filtering e plotting

Scrivere un **programma in C++** in cui dei punti letti da file vengono classificati in 2 categorie, dentro e fuori da un cerchio centrato nel piano `(x,y) = (0.5, 0.5)` e raggio `r = 0.5`. Programmare applicando la distinzione tra header e sorgenti.

1. Definire una struttura dati per punti sul piano `(x,y)`. Scaricare il file di dati con le coordinate `(x,y)` di 1000 punti con:
    ```
    wget https://raw.githubusercontent.com/scarrazza/informatica2021/master/Lezione_10/data1.dat
    # oppure
    curl https://raw.githubusercontent.com/scarrazza/informatica2021/master/Lezione_10/data1.dat -o data1.dat
    ```

2. Caricare i dati da file in un array dinamico della struttura definita al punto 1.

3. Per ogni elemento dell'array di punti determinare se si trova dentro o fuori del cerchio e stampare le coordinate `(x,y)` in 2 file distinti, rispettivamente `dentro.dat` e `fuori.dat`. *(**Suggerimento**: costruire una funzione che calcola la distanza tra il punto e il centro del cerchio in modo che il codice di filtraggio sia breve.)*

Scrivere uno script di plotting in cui:

4. Disegnare lo scatter plot dei punti in `dentro.dat` in blu e `fuori.dat` in rosso.

5. Aggiornare il titolo, ascisse e label (legenda) per entrambi tipi di punti.

6. Salvare il plot in un file `esercizio1.png`.

7. Mostrare il plot a schermo con `plt.show()`.

## Esercizio 2 - Error bar plot

Scrivere uno **script di plotting** per rappresentare le coordinate di un oggetto in moto uniformemente accelerato.

1. Scaricare il file di dati con le coordinate `(tempo,y(t))` di 100 punti:
    ```
    wget https://raw.githubusercontent.com/scarrazza/informatica2021/master/Lezione_10/data2.dat
    # oppure
    curl https://raw.githubusercontent.com/scarrazza/informatica2021/master/Lezione_10/data2.dat -o data2.dat
    ```

2. Caricare i dati considerando l'errore sull'asse `x` nullo, mentre quello sull'asse `y` costante e uguale a `yerr = 0.1`.

3. Aggiornare il titolo, ascisse e label.

4. Salvare il plot in un file `esercizio2.png`.

5. Mostrare il plot a schermo.

6. (Optional) Fittare i dati usando la forma parametrica `y(t) = 1/2 * a * t^2`, dove `a` è il parametro da ottimizzare. Stampare da terminale il chi2 e il valore finale di `a`. *Suggerimento* usare il modulo `scipy.optimize.curve_fit`.

## Esercizio 3 - Histograms

Scrivere uno **script di plotting** per .

1. Scaricare i dati con:
    ```
    wget https://raw.githubusercontent.com/scarrazza/informatica2021/master/Lezione_10/data3.dat
    # oppure
    curl https://raw.githubusercontent.com/scarrazza/informatica2021/master/Lezione_10/data3.dat -o data3.dat
    ```

2. Caricare i dati in un istogramma con 50 bins tra [-20, 25].

3. Disegnare l'istogramma, colorare e aggiungere il titolo.

4. Salvare il plot in un file `esercizio3.png`.

5. Mostrare il plot a schermo.

## Esercizio 4 - Data generator

Il file `/home/comune/20190718/data.dat`, presente sulla macchina `tolab.fisica.unimi.it`, contiene riga per riga la descrizione di un numero imprecisato di misure temporali di un oggetto in movimento sullo spazio tridimensionale effettuate in laboratorio. La prima colonna del file determina l'istante *t*, del vettore velocità *(vx, vy, vz)* sullo spazio tridimensionale, mentre l'ultima colonna contiene l'energia cinetica totale dell'oggetto all'istante *t*. Dunque, ogni rida del file `data.dat` contiene 1 dato di tipo `int` e 4 dati di tipo `double`.

Definita la struttura:
```c++
struct misure {
    int t;          // istante della misura
    double vx;      // coordinata vx dell'oggetto
    double vy;      // coordinata vx dell'oggetto
    double vz;      // coordinata vz dell'oggetto
    double K;       // energia cinetica totale dell'oggetto
    double massa;   // massa dell'oggetto in moto
};
```

Svolegere i seguenti punti con un programma in C++, usando la distinzione header/sorgente e makefile assieme ad un script di plotting:

1. Caricare tutte le misure descritte nel file `data.dat` in un array di misure allocato dinamicamente. Il
campo `massa` verrà riempito in seguito, inizializzarlo a zero durante il caricamento da file. Stampare
a video: (i) il numero di misure lette e (ii) la descrizione completa di ogni misura. *(**Hint**: scrivere funzioni per caricare l'array da file e per stampare la descrizione completa di ogni misura.)*

2. (i) Scrivere una funzione che calcola la massa per ogni instante *t* sapendo che l'energia cinetica è
    ```
    K = 1/2 * m * (vx^2 + vy^2 + vz^2),
    ```
    (ii) Assegnare a ciascuna misura la propria massa, cioè: assegnare al campo `massa` di misure.
    (iii) Stampare a video la descrizione aggiornata delle misure. *(**Hint**: usare la funzione del punto 1.)*

3. Disegnare l'istogramma delle masse calcolate al punto precedente usando 30 bins sul dominio [35, 100]. *(**Hint**: stampare le masse calcolate al punto precedente e caricarle sullo script di plotting.)*
