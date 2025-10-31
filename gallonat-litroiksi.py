# Funktio, joka muuntaa gallonat litroiksi
def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


# Pääohjelma
def main():
    while True:
        # Kysytään käyttäjältä bensiinin määrä
        gallonat = float(input("Anna bensiinin määrä (gallonoina, negatiivinen lopettaa): "))

        # Jos syöte on negatiivinen, lopetetaan ohjelma
        if gallonat < 0:
            print("Ohjelma päättyy.")
            break

        # Muunnetaan litroiksi ja tulostetaan tulos
        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat:.2f} gallonaa = {litrat:.2f} litraa\n")


# Käynnistetään pääohjelma
if __name__ == "__main__":
    main()
