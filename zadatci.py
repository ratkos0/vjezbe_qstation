import time
my_dict = {"name": "Ratko", "surname": "Sopic", "code": 1308}
print("Kreirani dictionary je ", my_dict)
print("Keys: ", my_dict.keys())
print("Values: ", my_dict.values())
print(my_dict)

unos = input("Unesite ime")
if unos != my_dict.get("name"):
    while unos.islower():
        print("Pobrinite se da je prvo slovo veliko")
        unos = input("Unesite ime")
    print("Korisnik u dictionari-ju nije prepoznati pa se dodaje novi..")
    time.sleep(2)
    nameinp = str(input("Vase ime?"))
    my_dict.update({"name": nameinp})
    surnameinp = str(input("Vase prezime?"))
    my_dict.update({"surname": surnameinp})
    codeinp = input("Unesite vasu lozinku.")
    my_dict.update({"code": codeinp})
    time.sleep(1)
    print(my_dict)
elif unos == my_dict.get("name"):
    print("Korisnik je pronadjen")
