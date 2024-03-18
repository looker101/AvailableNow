# **Creazione File Disponibile Subito**

:crocodile: | :whale2: | :shark: | :pretzel: | :cowboy_hat_face:
---

+ Esporta da Focus il file degli articoli della filiale I tramite Report > Magazzino > Solo Giacenze. Inseriscilo nella cartella "disponibili subito" e rinominalo in "Disponibili_subito_Focus".

+ Utilizza i file dei brand aggiornati presenti nella cartella "ok" dello scraping. Inseriscili nel seguente percorso: `C:\Users\miche\Desktop\.py\DisponibiliSubito\Brand`. Scegli i file dalla cartella più recente.

+ Il file `focus_compare.py` prende i file dei brand nella cartella Brand e li confronta con il file "Disponibili_subito_Focus". Sarà generato un file per ogni brand contenente gli articoli corrispondenti nel file di Focus.

+ Esegui il file `concat.py`. Questo programma concatena tutti i file presenti nella cartella "fileOK", creando un unico file consolidato.

+ Esegui il file `availableNow.py`. Questo script sostituirà il template esistente con "disponibili-subito", assicurando che i prodotti nel file siano associati al template corretto.

+ Il file `availableNow.py` aggiungerà inoltre il tag "available-now" ad ogni articolo.

+ Alla fine, verrà generato il file `AvailableNow.xlsx`, che dovrà essere importato su Shopify utilizzando Matrixify.

:alien: :skier: :climbing_man:

## File `main.py`

Esegui questo script per completare tutti i passaggi sopra elencati tramite un unico programma.
