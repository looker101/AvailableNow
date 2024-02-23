import pandas as pd
# scarica da matrixfy il file di ogni brand (oppure utilizza i file excel dello scraping)
# compara il file del brand col file di focus
# otterrai un file con tutti i prodotti in comune. Questi sono i prodotti disponibili subito di quel brand

# INSERISCI QUI L'INPUT!!!!
# Inserire come il brand come vedi anche nel file brand.txt
brand = str(input("Inserisci il brand: "))

# Inserisco il percorso da dove prendere il file del brand
path = "C:\\Users\\miche\\Desktop\\.py\\DisponibiliSubito\\Brand\\"

try:
    def disponibiliSubito():
        shopify = pd.read_excel(path+brand+".xlsx")
        focus = pd.read_excel("Disponibili_subito_Focus.xlsx")

        # colonne barcode
        focus.rename(columns={"Codice a barre":"Variant Barcode"}, inplace=True)

        # merge
        test = shopify.merge(focus, on="Variant Barcode", how="left", indicator=True)
        mask = test["_merge"] == "both"
        check = test[mask]

        check = check[[
        "ID", "Handle", "Command", "Title", "Body HTML", "Vendor", "Type", "Tags", "Tags Command", "Created At",
            "Updated At", "Status", "Published", "Published At", "Template Suffix", "URL", "Variant ID",
            "Variant SKU", "Variant Barcode", "Variant Price", "Variant Compare At Price", "Variant Inventory Qty",
            "Variant Inventory Adjust", "Inventory Available: +39 05649689443"
        ]]

        #check["Template Suffix"] = ""

        check.to_excel("C:\\Users\\miche\\Desktop\\.py\\DisponibiliSubito\\FileOK\\"+brand+".xlsx", index=False)

    if __name__ == "__main__":
        disponibiliSubito()
        print("File salvato nella cartella \"FileDisponibili\"")
    else:
        print("")
except FileNotFoundError as err:
    print("Hey, Mimmo!! Non hai inserito il file Matrixify!!!")