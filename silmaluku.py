import random

# Funktio, joka palauttaa satunnaisen nopan silmäluvun 1–6
def heita_noppaa():
    return random.randint(1, 6)

# Pääohjelma
def main():
    silmaluku = 0  # alustus
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print("Heiton tulos:", silmaluku)

# Käynnistetään pääohjelma
if __name__ == "__main__":
    main()
