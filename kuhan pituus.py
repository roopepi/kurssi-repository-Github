# Kysytään käyttäjältä kuhan pituus senttimetreinä
pituus = int(input("Anna kuhan pituus senttimetreinä: "))

# Määritä alamitta
alamitta = 37

# Tarkista, onko kuha alamittainen
if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen. Laske se takaisin järveen! Pituutta puuttuu {puuttuu} cm.")
else:
    print("Kuha on sallituissa mitoissa. Voit pitää sen.")
