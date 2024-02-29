import pandas as pd

path = "C:\\Users\\miche\\Desktop\\.py\\DisponibiliSubito\\FileOK\\"
path1 = "C:\\Users\\miche\\Desktop\\myVenv\\Disponibili_Subito\\FileDisponibili"

def concatFile():
    # creo un lista con i nomi dei file dei brand
    files = ["adidas_originals_ok.xlsx", "adidas_sport_ok.xlsx", "amq_ok.xlsx", "arnette_ok.xlsx",
             "bale_ok.xlsx", "bottega_ok.xlsx", "burberry_ok.xlsx", "carrera_ok.xlsx", "chloe_ok.xlsx",
             "david_beckham_ok.xlsx", "dolce_gabbana_ok.xlsx", "emporio_armani_ok.xlsx", "giorgio_armani_ok.xlsx",
             "gucci_ok.xlsx", "guess_ok.xlsx", "kate_spade_ok.xlsx", "miumiu_ok.xlsx", "mj_ok.xlsx",
             "monlcer_ok.xlsx", "mk_ok.xlsx", "oak_kids.xlsx", "oakley_ok.xlsx", "oakley_snow_ok.xlsx",
             "pld_ok.xlsx", "persol_ok.xlsx", "prada_ok.xlsx", "plr_ok.xlsx", "rayban_ok.xlsx",
             "rayban_kids_ok.xlsx", "rudy_project_ok.xlsx", "sl_ok.xlsx", "sk_ok.xlsx", "tiffany_ok.xlsx",
             "tb_ok.xlsx", "ft_ok.xlsx", "tommy_hilfiger_ok.xlsx", "underAmor_ok.xlsx", "versace_ok.xlsx", "vogue_ok.xlsx"]

    # creo lista vuota dove inserirò ogni dataframe per ogni brand
    dataframes = []
    for file in files:
        try:
            # creo un df per ogni brand concatenando il path al nome del file della lista
            df = pd.read_excel(path + file)
            # aggiungo il dataframe alla lista dataframes
            dataframes.append(df)
        except FileNotFoundError:
            print(f"File not found: {file}")

    if dataframes:
        # se la lista dataframes ha al suo interno dei valori, concatena questi valori
        availableNow = pd.concat(dataframes)
        # salvo il file
        availableNow.to_excel("Concat_File.xlsx", index=False)
        print(f"File salvato nella directory {path1}")
    else:
        print("Nessun file da concatenare.")
    return availableNow

if __name__ == "__main__":
    concatFile()