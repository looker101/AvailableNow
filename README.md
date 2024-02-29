:cowboy_hat_face:
# **Creazione file Disponibile subito**
---
- 1. Export da Focus del file degli articoli nella filiale I: Report > Magazzino > Solo Giacienze. Inseriscila nella cartella disponibili subito e rinomina il file "Disponibili_subito_Focus"
2. Usa i file dei brand aggiornati che si trovano nella cartella "ok" dello scraping e inseriscili qui: "C:\Users\miche\Desktop\.py\DisponibiliSubito\Brand". Utilizza quelli all'interno della cartella più recente. 
3. Il file focus compare prende i file dei brand nella cartella Brand e lo confronta con il file Disponibili_subito_Focus. Viene generato un file per ogni brand con gli articoli che corrispondono al file del focus.
4. Esegui il file concat.py: Queso programma concatena tutti i files presenti nella cartella fileOK, creando un unico file.
5. Esegui il file availableNow. Il file sostituirà il template esistente con "disponibili-subito" in modo che i prodotti nel file abbiano il corretto template
6. Il file availableNow aggiungerà anche il tag "available-now" ad ogni articolo.
7. Verrà generato il file AvailableNow.xlsx che dovrà essere importato su Shopify attraverso Matrixify
