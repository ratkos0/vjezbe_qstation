import sqlite3
import time
def unos():
    x = int(input("Koliko zelite clanova da unesete"))
    while x != 0:

        id = int(input('Unesite vas jedinstveni ID'))
        time.sleep(0.5)

        ime = str(input('Unesite Vase ime'))
        while ime.islower():
            print("Prvo slovo je veliko.")
            ime = str(input('Unesite Vase ime'))
        time.sleep(0.5)

        prezime = str(input('Unesite Vase prezime'))
        while prezime.islower():
            print("Prvo slovo je veliko..")
            prezime = str(input('Unesite Vase prezime'))
        time.sleep(0.5)

        polmz = str(input('Unesite Vas spol M/Z'))
        while polmz.islower():
            print("Ovo sllovo mora veliko biti..")
            polmz = str(input('Unesite Vas spol M/Z'))
        time.sleep(0.5)

        godine = str(input('Unesite koliko imate godina'))
        time.sleep(0.5)
        list = [(id, ime, prezime, polmz, godine)]
        connection.executemany("""INSERT INTO clanovi(id, first_name, last_name,pol, godine) VALUES (?,?,?,?,?)""",
                               list)
        x -= 1
        connection.commit()

connection = sqlite3.connect('qbase.db')

cursor = connection.cursor()

unos()


connection.close()