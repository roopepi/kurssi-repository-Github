import random

# Funktio, joka saa parametrina nopan tahkojen määrän
# ja palauttaa satunnaisen silmäluvun väliltä 1..tahkot
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

# Pääohjelma
def main():
    # Kysytään käyttäjältä nopan tahkojen määrä
    tahkot = int(input("Anna nopan tahkojen määrä: "))

    silmaluku = 0
    heittojen_maara = 0

    # Heitetään noppaa kunnes tulee suurin mahdollinen silmäluku
    while silmaluku != tahkot:
        silmaluku = heita_noppaa(tahkot)
        heittojen_maara += 1
        print(f"Heitto {heittojen_maara}: {silmaluku}")

    print(f"\nOnnittelut! Sait maksimisilmäluku {tahkot} {heittojen_maara}. heitolla.")

# Käynnistetään pääohjelma
if __name__ == "__main__":
    main()
