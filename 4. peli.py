import random

# Tietokone arpoo luvun 1–10
oikea_luku = random.randint(1, 10)

while True:
    try:
        arvaus = int(input("Arvaa luku väliltä 1–10: "))
    except ValueError:
        print("Anna kokonaisluku!")
        continue

    if arvaus < oikea_luku:
        print("Liian pieni arvaus")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus")
    else:
        print("Oikein!")
        break  # Arvattu oikein, lopetetaan peli
