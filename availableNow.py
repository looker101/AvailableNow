import pandas as pd
# quantità a 5
# template suffix = disponibili-subito

brand_file = pd.read_excel("Concat_File.xlsx")
focus = pd.read_excel("Disponibili_subito_Focus.xlsx")
#print(brand_file.columns)

def finalFile():
    #brand_file[["Variant Inventory Qty", "Inventory Available: +39 05649689443"]] = 1
    brand_file["Template Suffix"] = "disponibili-subito"
    brand_file["Tags"] = brand_file["Tags"].apply(lambda x : x + ", available now")
    #brand_file["Variant Inventory Qty"] = brand_file["Inventory Available: +39 05649689443"]
    # SCONTO
    #def discount(prezzo):
    #    return round(prezzo * 0.80)
    #rendo entrambe le colonne dei prezzi float64
    #prima riempio le celle vuote con 0
    # brand_file["Variant Compare At Price"] = brand_file["Variant Compare At Price"].fillna(0)
    # brand_file[["Variant Price", "Variant Compare At Price"]] = brand_file[["Variant Price", "Variant Compare At Price"]].astype("float64")
    # brand_file["Variant Price"] = brand_file["Variant Compare At Price"].apply(discount)

    brand_file.to_excel("AvailableNow.xlsx", index = False)

if __name__ == "__main__":
    finalFile()
    print("Il file è stato salvato correttamente!")