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



"""
class Trougao:
    def __init__(self, a=int, b=int, c=int):
        self.a = a
        self.b = b
        self.c = c

    def Info(self):
        print("Stranica a je:", self.a , " cm")
        print("Stranica b je:", self.b , " cm")
        print("Stranica c je:", self.c , " cm")


x = int(input("Koliko trouglova zelite da unesete(max=5)"))
if x == 5:
    print("Prvi prougao...")
    p2_a = int(input("Unesite stranicu a trougla."))
    p2_b = int(input("Unesite stranicu b trougla"))
    p2_c = int(input("Unesite stranicu c trougla"))
    pt2 = Trougao(p2_a, p2_b, p2_c)

    print("Drugi trougao...")
    p3_a = int(input("Unesite stranicu a trougla."))
    p3_b = int(input("Unesite stranicu b trougla"))
    p3_c = int(input("Unesite stranicu c trougla"))
    pt3 = Trougao(p3_a, p3_b, p3_c)

    print("Treci trougao...")
    p4_a = int(input("Unesite stranicu a trougla."))
    p4_b = int(input("Unesite stranicu b trougla"))
    p4_c = int(input("Unesite stranicu c trougla"))
    pt4 = Trougao(p4_a, p4_b, p4_c)

    print("Cetvrti trougao...")
    p5_a = int(input("Unesite stranicu a trougla."))
    p5_b = int(input("Unesite stranicu b trougla"))
    p5_c = int(input("Unesite stranicu c trougla"))
    pt5 = Trougao(p5_a, p5_b, p5_c)

    print("Peti trougao...")
    p6_a = int(input("Unesite stranicu a trougla."))
    p6_b = int(input("Unesite stranicu b trougla"))
    p6_c = int(input("Unesite stranicu c trougla"))
    pt6 = Trougao(p6_a, p6_b, p6_c)
    print("-------------------")
    pt2.Info()
    print("-------------------")
    pt3.Info()
    print("-------------------")
    pt4.Info()
    print("-------------------")
    pt5.Info()
    print("-------------------")
    pt6.Info()
    print("-------------------")


elif x == 4:
    print("Prvi prougao...")
    p2_a = int(input("Unesite stranicu a trougla."))
    p2_b = int(input("Unesite stranicu b trougla"))
    p2_c = int(input("Unesite stranicu c trougla"))
    pt2 = Trougao(p2_a, p2_b, p2_c)

    print("Drugi trougao...")
    p3_a = int(input("Unesite stranicu a trougla."))
    p3_b = int(input("Unesite stranicu b trougla"))
    p3_c = int(input("Unesite stranicu c trougla"))
    pt3 = Trougao(p3_a, p3_b, p3_c)

    print("Treci trougao...")
    p4_a = int(input("Unesite stranicu a trougla."))
    p4_b = int(input("Unesite stranicu b trougla"))
    p4_c = int(input("Unesite stranicu c trougla"))
    pt4 = Trougao(p4_a, p4_b, p4_c)

    print("Cetvrti trougao...")
    p5_a = int(input("Unesite stranicu a trougla."))
    p5_b = int(input("Unesite stranicu b trougla"))
    p5_c = int(input("Unesite stranicu c trougla"))
    pt5 = Trougao(p5_a, p5_b, p5_c)
    print("-------------------")
    pt2.Info()
    print("-------------------")
    pt3.Info()
    print("-------------------")
    pt4.Info()
    print("-------------------")
    pt5.Info()
    print("-------------------")

elif x == 3:
    print("Prvi prougao...")
    p2_a = int(input("Unesite stranicu a trougla."))
    p2_b = int(input("Unesite stranicu b trougla"))
    p2_c = int(input("Unesite stranicu c trougla"))
    pt2 = Trougao(p2_a, p2_b, p2_c)

    print("Drugi trougao...")
    p3_a = int(input("Unesite stranicu a trougla."))
    p3_b = int(input("Unesite stranicu b trougla"))
    p3_c = int(input("Unesite stranicu c trougla"))
    pt3 = Trougao(p3_a, p3_b, p3_c)

    print("Treci trougao...")
    p4_a = int(input("Unesite stranicu a trougla."))
    p4_b = int(input("Unesite stranicu b trougla"))
    p4_c = int(input("Unesite stranicu c trougla"))
    pt4 = Trougao(p4_a, p4_b, p4_c)
    print("-------------------")
    pt2.Info()
    print("-------------------")
    pt3.Info()
    print("-------------------")
    pt4.Info()
    print("-------------------")


elif x == 2:
    print("Prvi prougao...")
    p2_a = int(input("Unesite stranicu a trougla."))
    p2_b = int(input("Unesite stranicu b trougla"))
    p2_c = int(input("Unesite stranicu c trougla"))
    pt2 = Trougao(p2_a, p2_b, p2_c)

    print("Drugi trougao...")
    p3_a = int(input("Unesite stranicu a trougla."))
    p3_b = int(input("Unesite stranicu b trougla"))
    p3_c = int(input("Unesite stranicu c trougla"))
    pt3 = Trougao(p3_a, p3_b, p3_c)
    print("-------------------")
    pt2.Info()
    print("-------------------")
    pt3.Info()
    print("-------------------")


elif x == 1:
    print("Prvi prougao...")
    p2_a = int(input("Unesite stranicu a trougla."))
    p2_b = int(input("Unesite stranicu b trougla"))
    p2_c = int(input("Unesite stranicu c trougla"))
    pt2 = Trougao(p2_a, p2_b, p2_c)
    print("-------------------")
    pt2.Info()
    print("-------------------")
"""
