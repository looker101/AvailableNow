import pandas as pd

path = "C:\\Users\\miche\\Desktop\\myVenv\\Disponibili_Subito\\Brand\\"
path1 = "C:\\Users\\miche\\Desktop\\myVenv\\Disponibili_Subito\\FileDisponibili"

# concatenazione di tutti i file di Shopify
# creazione del file finale di shopify da comparare a quello del Focus

def concatFile():
    adidas = pd.read_excel(path+"adidas_originals.xlsx")
    amq = pd.read_excel(path+"amq.xlsx")
    arnette = pd.read_excel(path+"arnette.xlsx")
    balenciga = pd.read_excel(path+"balenciaga.xlsx")
    bottega = pd.read_excel(path+"bottega.xlsx")
    burberry = pd.read_excel(path+"burberry.xlsx")
    chloe = pd.read_excel(path+"chloe.xlsx")
    emporio = pd.read_excel(path+"emporio.xlsx")
    giorgio = pd.read_excel(path+"giorgio.xlsx")
    gucci = pd.read_excel(path+"gucci.xlsx")
    guess = pd.read_excel(path+"guess.xlsx")
    miu = pd.read_excel(path+"miu.xlsx")
    monlcer = pd.read_excel(path+"moncler.xlsx")
    oakley = pd.read_excel(path+"oakley.xlsx")
    oakleySnow = pd.read_excel(path+"oakleySnow.xlsx")
    persol = pd.read_excel(path+"persol.xlsx")
    prada = pd.read_excel(path+"prada.xlsx")
    rayban = pd.read_excel(path+"rayban.xlsx")
    rudy = pd.read_excel(path+"rudyProject.xlsx")
    saintLaurent = pd.read_excel(path+"saintLaurent.xlsx")
    swarowski = pd.read_excel(path+"swarovski.xlsx")
    tiffany = pd.read_excel(path+"tiffany.xlsx")
    timberland = pd.read_excel(path+"timberland.xlsx")
    tommy = pd.read_excel(path+"tommy.xlsx")
    versace = pd.read_excel(path+"versace.xlsx")
    vogue = pd.read_excel(path+"vogue.xlsx")

    availablaNow = pd.concat([
    adidas, amq, arnette, balenciga, bottega, burberry, chloe, emporio, giorgio, gucci,
        guess, miu, monlcer, oakley, oakleySnow, persol, prada, rayban, rudy, saintLaurent,
        swarowski, tiffany, timberland, tommy, versace, vogue
    ])
    availablaNow.to_excel("Concat_File.xlsx", index=False)

if __name__ == "__main__":
    concatFile()
    print(f"File salvato nella directory {path1}")