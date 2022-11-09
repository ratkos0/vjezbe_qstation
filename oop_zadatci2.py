"""class Napitak:
    def __init__(self, kolicina, naziv):
        self.kolicina = kolicina
        self.naziv = naziv


    def __str__(self):
        return "Kolicina: " + str(self.kolicina) + "L" + "\nNaziv:" + str(self.naziv)


class Alkohol(Napitak):

    def __init__(self, naziv, kolicina, kolicina_alkohola):
        Napitak.__init__(self, naziv, kolicina)
        self.kolicina_alkohola = kolicina_alkohola

    def __str__(self):
        return str(Napitak.__str__(self)) + "\nKolicina alkohola: " + str(self.kolicina_alkohola) +"%"




listaAlkohola = []


class Sok:

    def __init__(self, kolicina, naziv, kolicina_secera):
        Napitak.__init__(self, kolicina, naziv)
        self.kolicina_secera = kolicina_secera

    def __str__(self):
        return str(Napitak.__str__(self)) + "\nKolicina secera: " + str(self.kolicina_secera) + "grama"

listaSokova = []


n1 = int(input("Unesite broj alkholnih pica"))

while n1 > 0:
    alkos_ime = input("Unesite ime")
    alkos_kolicina = float(input("Unesite kolicinu pica u litrima -->"+ alkos_ime))
    alkos_post = (input("Unesite postotak alkohola(samo broj)"))
    pice = Alkohol(alkos_kolicina, alkos_ime, alkos_post)
    listaAlkohola.append(pice)
    n1 -=1

s1 = int(input("Unesite broj sokova"))

while s1 > 0:
    sok_ime = input("Unesite ime")
    sok_kolicina = float(input("Unesite kolicinu pica u litrima -->"+ sok_ime))
    sok_secer = (input("Unesite kolicinu secera u gramima"))
    sok = Sok(sok_kolicina, sok_ime, sok_secer)
    listaSokova.append(sok)
    s1 -=1

for l in listaAlkohola:
    print(l)
for s in listaSokova:
    print(s)

"""


