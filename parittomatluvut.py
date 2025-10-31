# Funktio, joka poistaa listasta parittomat luvut
def poista_parittomat(luvut):
    # Palautetaan uusi lista, jossa on vain parilliset luvut
    return [luku for luku in luvut if luku % 2 == 0]

# Pääohjelma
def main():
    # Luodaan testilista
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Kutsutaan funktiota
    karsittu_lista = poista_parittomat(alkuperainen_lista)

    # Tulostetaan molemmat listat
    print("Alkuperäinen lista:", alkuperainen_lista)
    print("Parittomat luvut poistettu:", karsittu_lista)

# Käynnistetään pääohjelma
if __name__ == "__main__":
    main()
