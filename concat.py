import pandas as pd

path = "C:\\Users\\miche\\Desktop\\.py\\DisponibiliSubito\\FileOK\\"
path1 = "C:\\Users\\miche\\Desktop\\myVenv\\Disponibili_Subito\\FileDisponibili"

# concatenazione di tutti i file di Shopify
# creazione del file finale di shopify da comparare a quello del Focus

def concatFile():
    adidas = pd.read_excel(path+"adidas_originals_ok.xlsx")
    amq = pd.read_excel(path+"amq_ok.xlsx")
    arnette = pd.read_excel(path+"arnette_ok.xlsx")
    balenciga = pd.read_excel(path+"bale_ok.xlsx")
    bottega = pd.read_excel(path+"bottega_ok.xlsx")
    burberry = pd.read_excel(path+"burberry_ok.xlsx")
    chloe = pd.read_excel(path+"chloe_ok.xlsx")
    emporio = pd.read_excel(path+"emporio_armani_ok.xlsx")
    giorgio = pd.read_excel(path+"giorgio_armani_ok.xlsx")
    gucci = pd.read_excel(path+"gucci_ok.xlsx")
    guess = pd.read_excel(path+"guess_ok.xlsx")
    miu = pd.read_excel(path+"miumiu_ok.xlsx")
    monlcer = pd.read_excel(path+"monlcer_ok.xlsx")
    oakley = pd.read_excel(path+"oakley_ok.xlsx")
    oakleySnow = pd.read_excel(path+"oakley_snow_ok.xlsx")
    persol = pd.read_excel(path+"persol_ok.xlsx")
    prada = pd.read_excel(path+"prada_ok.xlsx")
    rayban = pd.read_excel(path+"rayban_ok.xlsx")
    rudy = pd.read_excel(path+"rudy_project_ok.xlsx")
    saintLaurent = pd.read_excel(path+"sl_ok.xlsx")
    swarowski = pd.read_excel(path+"sk_ok.xlsx")
    tiffany = pd.read_excel(path+"tiffany_ok.xlsx")
    timberland = pd.read_excel(path+"tb_ok.xlsx")
    tommy = pd.read_excel(path+"tommy_hilfiger_ok.xlsx")
    versace = pd.read_excel(path+"versace_ok.xlsx")
    vogue = pd.read_excel(path+"vogue_ok.xlsx")

    availablaNow = pd.concat([
    adidas, amq, arnette, balenciga, bottega, burberry, chloe, emporio, giorgio, gucci,
        guess, miu, monlcer, oakley, oakleySnow, persol, prada, rayban, rudy, saintLaurent,
        swarowski, tiffany, timberland, tommy, versace, vogue
    ])
    availablaNow.to_excel("Concat_File.xlsx", index=False)

if __name__ == "__main__":
    concatFile()
    print(f"File salvato nella directory {path1}")