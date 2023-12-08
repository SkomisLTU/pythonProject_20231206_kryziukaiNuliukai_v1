### 2023 12 6
#
## kryziukai nuliukai zaidimas
#
'''
saltiniai:

cursor position:
https://stackoverflow.com/questions/3698635/how-to-get-the-text-cursor-position-in-windows

kaip isvalyti konsole:
'''

from modules.matrica import matrica
import os

rezultatas = {"Kryžiukai": 0, "Nuliukai": 0}
ejimas = 0
laimejo = False

### exe failui
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

zaidimas1 = matrica()
zaidimas1.pridetRema(ejimas)

# kol nelaimejo
while not laimejo:
    # X ejimas

    zaidimas1.uzbraukti("X")
    ejimas = zaidimas1.pridetRema(ejimas)
    if ejimas > 4:   # nes laimeti galima tik po 5 ejimo
        if zaidimas1.arlaimejo("X"):
            print("Kryziukai laimojo! :) ")
            break
        elif ejimas > 8:
            print("Lygiosios! :) ")
            break

    # Y ejimas

    zaidimas1.uzbraukti("O")
    ejimas = zaidimas1.pridetRema(ejimas)
    if ejimas > 4:
        if zaidimas1.arlaimejo("O"):
            print("Nuliukai laimojo! :) ")
            break









