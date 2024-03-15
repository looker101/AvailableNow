from focus_compare import disponibiliSubito, files_brand
from concat import concatFile
from availableNow import finalFile

if __name__ == "__main__":
    for file_brand in files_brand:
        try:
            disponibiliSubito(file_brand)
            print(f"{file_brand} inserito nella cartella 'ok'")
        except Exception as e:
            print(f"Errore durante l'elaborazione dei file : {e}")

    try:
        concatFile()
    except Exception as err:
        print(f"Qualcosa è andato storto durante la concatenazione: {err}")
        
    else:
        finalFile()