# Funktio, joka palauttaa listassa olevien lukujen summan
def laske_summa(numerot):
    return sum(numerot)

# Pääohjelma
def main():
    # Luodaan lista kokonaisluvuista
    luvut = [3, 7, 2, 8, 5]

    # Kutsutaan funktiota ja tallennetaan tulos
    tulos = laske_summa(luvut)

    # Tulostetaan tulos
    print("Listan luvut:", luvut)
    print("Lukujen summa on:", tulos)

# Käynnistetään pääohjelma
if __name__ == "__main__":
    main()
