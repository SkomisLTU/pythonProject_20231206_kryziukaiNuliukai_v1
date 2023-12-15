import msvcrt
import time


class Matrica:

    RAUDONA   = '\033[91m'
    ZALIA   = '\033[92m'
    GELTONA     = '\033[93m'
    MELYNA    = '\033[94m'
    VIOLETINE = '\033[95m'
    ENC = '\033[0m'   #  end of colour
    vardai = ["",""]  ## indeksas 0 -> iksiuku zaidejas, 1 -> nuliuku zaidejas



    def __init__(self):
        print("\n"*10)   ### kad nesimaisytu senos lenteles
        self.pradinis = ["1", "2", "3",
                         "4", "5", "6",
                         "7", "8", "9"]

    def uzbraukti(self, ka_braukti):

        self.ka_braukti = ka_braukti

        a = ""

        while 1:
            if self.ka_braukti == "X":
                ## zodis, spalva, vardas, end of colour
                print("Žaidžia ", self.VIOLETINE, self.vardai[0], ":\t", self.ENC)
                a = input()
                spal = self.VIOLETINE
            elif self.ka_braukti == "O":
                print("Žaidžia ", self.GELTONA, self.vardai[1], ":\t", self.ENC)
                a = input()
                spal = self.GELTONA
            elif self.ka_braukti == "K": ## kompiuteris
                print(self.vardai[1], " galvoja")
                time.sleep(2)
                count = (int(time.time_ns()/1000)%9)  ## random skaicius naudojant sistemos laika
                ## ziuri ar sugeneruotas ejimas laisvas
                while not self.pradinis[count] == str(count+1):
                    count = int(time.time_ns() / 1000) % 9
                a = str(count+1)
                spal = self.MELYNA
            else:
                print("kazkas blogai")
                break
        ### paziuri ar ivestas skaicius nuo 1 iki 9 ir ar nesikartoja
            if a.isdigit() and int(a) >=1 and int(a) < 10 and self.pradinis[int(a)-1].isdigit():
                if (ka_braukti == "K"):  ### jeigu zaidziam su kompu vistiek rasom nuliuka
                    ka_braukti = "O"
                self.pradinis[int(a)-1] = spal + ka_braukti + self.ENC    ## spalva + keiciamas skaicius + end of colour
                break
            else:
                print("blogas ejimas, spauskite dar kartelį")


    def pridetRema(self, kartas):
        s = "\n" * 5
        s += "_______________\n"
        s += self.pradinis[6]   # 7
        s += "  |  "
        s += self.pradinis[7]   # 8
        s += "  |  "
        s += self.pradinis[8]   # 9
        s += "\n---------------\n"
        s += self.pradinis[3]   # 4
        s += "  |  "
        s += self.pradinis[4]   # 5
        s += "  |  "
        s += self.pradinis[5]   # 6
        s += "\n---------------\n"
        s += self.pradinis[0]   # 1
        s += "  |  "
        s += self.pradinis[1]   # 2
        s += "  |  "
        s += self.pradinis[2]   # 3
        s += "\n \u0304 \u0304 \u0304 \u0304 \u0304 \u0304 \u0304 "
        s += "\u0304 \u0304 \u0304 \u0304 \u0304 \u0304 \u0304 \u0304"

        print(s)

        return kartas + 1

    def arlaimejo(self, kas):
        laimejo = False
        if ((self.pradinis[0].count(kas) and self.pradinis[1].count(kas) and self.pradinis[2].count(kas))    # tikrinam eilutes
            or (self.pradinis[3].count(kas) and self.pradinis[4].count(kas) and self.pradinis[5].count(kas)) #
            or (self.pradinis[6].count(kas) and self.pradinis[7].count(kas) and self.pradinis[8].count(kas)) ####
            or (self.pradinis[0].count(kas) and self.pradinis[3].count(kas) and self.pradinis[6].count(kas)) # tikrinam stulpelius
            or (self.pradinis[1].count(kas) and self.pradinis[4].count(kas) and self.pradinis[7].count(kas)) #
            or (self.pradinis[2].count(kas) and self.pradinis[5].count(kas) and self.pradinis[8].count(kas)) #
            or (self.pradinis[0].count(kas) and self.pradinis[4].count(kas) and self.pradinis[8].count(kas)) # tikrinam istrizaines
            or (self.pradinis[6].count(kas) and self.pradinis[4].count(kas) and self.pradinis[2].count(kas))): #
            laimejo = True

        return laimejo
