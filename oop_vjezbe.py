"""class Ptica:
    def __init__(self, boja, sirinakrila, naziv, staniste):
        self.boja = boja
        self.sirinakrila = sirinakrila
        self.naziv = naziv
        self.staniste = staniste

    def Info(self):
        print("Naziv: ", self.naziv)
        print("Boja: ", self.boja)
        print("Sirina krila: ", self.sirinakrila)
        print("Staniste: ", self.staniste)



class Mlade(Ptica):
    def __init__(self, boja, sirinakrila, naziv, staniste, starost):
        Ptica.__init__(self, boja, sirinakrila, naziv, staniste)
        self.starost = starost

    def Info(self):
        Ptica.Info(self)
        print("Starost: ", self.starost)


n1 = Mlade("Crna", 28, "Kos", "Sumarci, livade i gradovi", 1)
n2 = Ptica("Crna", 28, "Kos", "Sumarci, livade i gradovi")

n1.Info()
n2.Info()"""

"""import time
class Osoba:
    def __init__(self, ime, prezime, jmbg, visina, tezina, godine):
        self.ime = ime
        self.prezime = prezime
        self.jmbg = jmbg
        self.tezina = tezina
        self.visina = visina
        self.godine = godine

    def Info(self):
        print("Ime: ", self.ime)
        time.sleep(0.5)
        print("Prezime:", self.prezime)
        print("JMBG:", self.jmbg)
        time.sleep(0.5)
        print("Visina:", self.visina)
        print("Tezina:", self.tezina)
        time.sleep(0.5)
        print("Godine:", self.godine)
        if self.godine >= 18:
            print("Osoba je punoljetna")
        elif self.godine >= 65:
            print("Osoba je penzioner")
        else:
            print("Osoba je maloljetna")

o1 = Osoba("Ratko", "Sopic", 2709000100001, 193, 83, 22)

o1.Info()
"""


"""class Trougao:
    def __init__(self, a=int, b=int, c=int):
        self.a = a
        self.b = b
        self.c = c

    def Info(self):
        print("Stranica a je:", self.a , " cm")
        print("Stranica b je:", self.b , " cm")
        print("Stranica c je:", self.c , " cm")


p1_a = int(input("Unesite stranicu a trougla."))
p1_b = int(input("Unesite stranicu b trougla"))
p1_c = int(input("Unesite stranicu c trougla"))

pt1 = Trougao(p1_a, p1_b, p1_c)
pt1.Info()"""
