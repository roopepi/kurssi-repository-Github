# Muunnoskerroin
MUUNNOSKERROIN = 2.54

# Kysy käyttäjältä ensimmäinen tuumamäärä
tuumat = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))

# Toistetaan niin kauan kuin tuumamäärä on positiivinen tai nolla
while tuumat >= 0:
    sentit = tuumat * MUUNNOSKERROIN
    print(f"{tuumat} tuumaa on {sentit:.2f} senttimetriä.\n")

    # Kysy uusi tuumamäärä
    tuumat = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))

# Kun käyttäjä antaa negatiivisen arvon, ohjelma päättyy
print("Ohjelma lopetettu.")
