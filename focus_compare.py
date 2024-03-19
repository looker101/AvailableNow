import pandas as pd
import os

# Percorso della cartella dove sono situati i file dei brand e dove salvare i risultati
path_brand = "C:\\Users\\miche\\Desktop\\.py\\DisponibiliSubito\\Brand\\"
path_ok = "C:\\Users\\miche\\Desktop\\.py\\DisponibiliSubito\\FileOK"

# Percorso del file Disponibili_subito_Focus.xlsx
path_focus = "Disponibili_subito_Focus.xlsx"

# Carica il file Disponibili_subito_Focus.xlsx una sola volta, fuori dal ciclo
focus = pd.read_excel(path_focus)
focus.rename(columns={"Codice a barre":"Variant Barcode"}, inplace=True)
focus["Variant Barcode"] = focus["Variant Barcode"].astype(str)

# Lista di tutti i file .xlsx nella cartella 'brand', escludendo il file Disponibili_subito_Focus.xlsx se presente
files_brand = [f for f in os.listdir(path_brand) if f.endswith('.xlsx') and f != "Disponibili_subito_Focus.xlsx"]

def disponibiliSubito(file_brand):
    shopify = pd.read_excel(os.path.join(path_brand, file_brand))
    shopify["Variant Barcode"] = shopify["Variant Barcode"].astype(str)
    shopify["Variant Barcode"] = shopify["Variant Barcode"].str.replace(".0", "")
    # merge
    check = shopify.merge(focus[['Variant Barcode', 'Quantità magazzino']], on="Variant Barcode", how="inner", indicator=True)
    check["Inventory Available: +39 05649689443"] = check["Quantità magazzino"]
    #mask = test["_merge"] == "both"
    #check = test[mask]

    check = check[[
    "ID", "Handle", "Command", "Title", "Body HTML", "Vendor", "Type", "Tags", "Tags Command", "Created At",
        "Updated At", "Status", "Published", "Published At", "Template Suffix", "URL", "Variant ID",
        "Variant SKU", "Variant Barcode", "Variant Price", "Variant Compare At Price", "Variant Inventory Qty",
        "Variant Inventory Adjust", "Inventory Available: +39 05649689443"
    ]]

    # Salva il risultato nella cartella FileOK con lo stesso nome del file di origine
    check.to_excel(os.path.join(path_ok, file_brand), index=False)

#if __name__ == "__main__":
#    for file_brand in files_brand:
#        try:
#            disponibiliSubito(file_brand)
#            print(f"File {file_brand} salvato nella cartella \"FileOK\"")
#        except Exception as e:
#            print(f"Errore durante l'elaborazione del file {file_brand}: {e}")
