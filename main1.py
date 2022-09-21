import time

samoglasnici = "a","e","i","o","u"

def name_info():
    print("Uneseno ime: "+ name.__str__()+" "+surname.__str__())
    time.sleep(0.5)
    print("Inicijali: "+ name[0],surname[0])
    time.sleep(0.5)
    print(name.replace(first_letter,first_letter_sur), surname.replace(first_letter_sur,first_letter))
    time.sleep(0.5)
    print("Završava li se ime samoglasnikom? ", name.endswith(samoglasnici), "A prezime?", surname.endswith(samoglasnici))
    time.sleep(0.5)
    #Ima neki problem
    print("Ima li samoglasnika u imenu? ", surname.count(str(samoglasnici)))
    time.sleep(0.5)
    print("Tip: ",type(name),type(surname))

name = str(input("Unesite Vaše ime."))
first_letter = name[0]
while name.isnumeric():
    print("Brojevi nisu dozvoljeni.")
    f = open("logger.txt", "a")
    f.write("\nPogrešan unos detektovan..")
    f.close()
    name = input("Unesite Vaše ime.")
time.sleep(0.5)
surname = str(input("Unesite Vaše prezime."))
first_letter_sur = surname[0]
while surname.isnumeric():
    print("Brojevi nisu dozvoljeni.")
    f = open("logger.txt", "a")
    f.write("\nPogrešan unos detektovan..")
    f.close()
    surname = input("Unesite Vaše prezime.")
time.sleep(2)



print(name_info())
