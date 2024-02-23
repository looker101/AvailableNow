import pandas as pd
# quantità a 5
# template suffix = disponibili-subito

df = pd.read_excel("Concat_File.xlsx")
#print(df.columns)

def finalFile():
    df[["Variant Inventory Qty", "Inventory Available: +39 05649689443"]] = 1
    df["Template Suffix"] = "disponibili-subito"
    df["Tags"] = df["Tags"].apply(lambda x : x + ", available now")
    # SCONTO
    #def discount(prezzo):
    #    return round(prezzo * 0.80)
    #rendo entrambe le colonne dei prezzi float64
    #prima riempio le celle vuote con 0
    # df["Variant Compare At Price"] = df["Variant Compare At Price"].fillna(0)
    # df[["Variant Price", "Variant Compare At Price"]] = df[["Variant Price", "Variant Compare At Price"]].astype("float64")
    # df["Variant Price"] = df["Variant Compare At Price"].apply(discount)

    df.to_excel("AvailableNow.xlsx", index = False)

if __name__ == "__main__":
    finalFile()
    print("Il tuo file è stato salvato correttamente!")