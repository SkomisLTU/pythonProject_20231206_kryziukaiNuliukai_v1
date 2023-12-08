class matrica:

    def __init__(self):
        print("\n"*10)
        self.pradinis = ["1", "2", "3",
                         "4", "5", "6",
                         "7", "8", "9"]

    def uzbraukti(self, ka_braukti):


        self.ka_braukti = ka_braukti
        a = ""
        while 1:
            if self.ka_braukti == "X":
                a = input("Žaidžia Kryziukai:\t")
            elif self.ka_braukti == "O":
                a = input("Žaidžia nuliukai:\t")
            else:
                print("kazkas blogai")
                break
        ### paziuri ar ivestas skaicius nuo 1 iki 9 ir ar nesikartoja
            if a.isdigit() and int(a) >=1 and int(a) < 10 and self.pradinis[int(a)-1].isdigit():
                self.pradinis[int(a)-1] = ka_braukti
                break
            else:
                print("blogas ejimas")


    def pridetRema(self, kartas):

        s = "_______________\n"
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
        if ((self.pradinis[0] == kas and self.pradinis[1] == kas and self.pradinis[2] == kas)    # tikrinam eilutes
            or (self.pradinis[3] == kas and self.pradinis[4] == kas and self.pradinis[5] == kas) #
            or (self.pradinis[6] == kas and self.pradinis[7] == kas and self.pradinis[8] == kas) ####
            or (self.pradinis[0] == kas and self.pradinis[3] == kas and self.pradinis[6] == kas) # tikrinam stulpelius
            or (self.pradinis[1] == kas and self.pradinis[4] == kas and self.pradinis[7] == kas) #
            or (self.pradinis[2] == kas and self.pradinis[5] == kas and self.pradinis[8] == kas) #
            or (self.pradinis[0] == kas and self.pradinis[4] == kas and self.pradinis[8] == kas) # tikrinam istrizaines
            or (self.pradinis[6] == kas and self.pradinis[4] == kas and self.pradinis[2] == kas)): #
            laimejo = True

        return laimejo
