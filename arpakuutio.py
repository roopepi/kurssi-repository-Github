import random

# Kysytään käyttäjältä arpakuutioiden määrä
lukumaara = int(input("Kuinka monta arpakuutiota heitetään? "))

# Alustetaan summa
summa = 0

# Heitetään arpakuutiot for-toistorakenteella
for i in range(lukumaara):
    heitto = random.randint(1, 6)  # Arpakuutio antaa silmäluvun 1–6
    summa += heitto

# Tulostetaan silmälukujen summa
print(f"Silmälukujen summa on {summa}.")
