### 2023 12 6
#
## kryziukai nuliukai zaidimas
#
'''
spalvotas terminal tekstas:
https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
'''

### importai
from modules.matrica import Matrica
import os as win10
import time

ejimas = 0
laimejo = False


### galima pridet exe failui, pycharmo konselej neveikia
def cls():
    win10.system('cls' if win10.name=='nt' else 'clear')


def meniu():
    print("iveskite komandą:")
    print("z -> žaisti 2 žaidėjams\tk -> žaisti su kompiuteriu")
    print("i -> info kaip žaisti\tu -> uždaryti programą")
    komanda = input("")
    match komanda:
        case "z":
            ejimas = 0
            zaidimas1 = Matrica()
            zaidimas1.pridetRema(ejimas)
            zaidimas1.vardai[0] = input("1 žaidėjo vardas:\t")
            zaidimas1.vardai[1] = input("2 žaidėjo vardas:\t")
            zaidimas1.vardai[1][0] =zaidimas1.vardai[1][1].upper()
            zaidimas1.vardai[1][1] =zaidimas1.vardai[1][1].upper()
            zaidziam(zaidimas1, ejimas, result=[0,0]) ## vardu nemetam, nes imetem visa objekta zaidimas1

        case "u":
            print("Ar tikrai norite uždaryti programą? :(\n y - taip\t n - ne")
            komanda2 = input("")
            if komanda2 == "y":
                print("Dėkojame, jog žaidėte :)")
                time.sleep(3)
                exit()
            else:
                meniu()
        case "k":
            ejimas = 0
            zaidimas1 = Matrica()
            zaidimas1.pridetRema(ejimas)
            zaidimas1.vardai[0] = input("1 žaidėjo vardas:\t")
            zaidimas1.vardai[1] = "Kompiuteris " + win10.getcwd().split("\\")[2]  ## kompo pavadinimas
            zaidziam(zaidimas1, ejimas, False, "X", "K")  ## vardu nemetam, nes imetem visa objekta zaidimas1
        case "i":
            if win10.name == "nt":   ### win10 pavadinimas
                try:
                    win10.system("start \"\" https://www.youtube.com/watch?v=0y0-xr2Af4w")
                except:
                    print("nepavyko atidaryti :(")
            elif win10.name == "pofix":       ### linux ir macos
                try: ## linux
                    win10.system("xdg-open \"\" https://www.youtube.com/watch?v=0y0-xr2Af4w")
                except:
                    print("nepavyko atidaryti :(")
                try:  ## macOs
                    win10.system("open \"\" https://www.youtube.com/watch?v=0y0-xr2Af4w")
                except:
                    print("nepavyko atidaryti :(")
        case _:
            print("Bloga komanda. Rinkitės dar kartą")
            meniu()

def zaidziam(zaidimas: Matrica, ejimas, pradedaO = False, zaid1= "X", zaid2= "O", result= [0,0]):
    print("res ", result, "  ", end="")
    b = pradedaO
    while not laimejo:
        # X ejimas
        if not b:   ### jeigu pradeda ne nuliukai
            zaidimas.uzbraukti(zaid1)
            ejimas = zaidimas.pridetRema(ejimas)
            if ejimas > 4:  # nes laimeti galima tik po 5 ejimo
                if zaidimas.arlaimejo(zaid1):
                    ## teksto spalva, vardas, tekstas, spalvos pabaiga
                    print(Matrica.VIOLETINE, zaidimas.vardai[0], " laimėjo! :) ", Matrica.ENC)
                    result[0] += 1
                    break
                elif ejimas > 8:
                    print(Matrica.ZALIA, "Lygiosios! :) ", Matrica.ENC)
                    break
        b = False
        # O ejimas

        zaidimas.uzbraukti(zaid2)
        ejimas = zaidimas.pridetRema(ejimas)
        if ejimas > 4:
            if zaidimas.arlaimejo(zaid2):
                print(Matrica.GELTONA, zaidimas.vardai[1], " laimėjo! :) ", Matrica.ENC)
                result[1] += 1
                break


    ### kita zaidima zaidejai apsikeicia
    print("ar žaisti dar kartą?\n [y > taip,n > ne]")
    match input():
        case "y":
            ## X su O apsikeicia vietomis, klase persiraso ir vel zaidzia
            print("Rezultatai: ", zaidimas.vardai[0], ": ", result[0], "\n         ",
                  zaidimas.vardai[1], ": ", result[1])
            zaidimas.__init__()
            zaidimas.pridetRema(0)
            zaidziam(zaidimas, 0, not(pradedaO), zaid1, zaid2, result=[result[0],result[1]])
        case _:
            print("Rezultatai: ", zaidimas.vardai[0], ": ", result[0], "\n         ",
                  zaidimas.vardai[1], ": ", result[1])
            meniu() ## inicijuojam is naujo


##
### init
##

print("\t\tSveiki atvykę!")
meniu()

