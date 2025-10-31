import math

# Funktio, joka laskee pizzan yksikköhinnan euroina per neliömetri
def laske_yksikkohinta(halkaisija_cm, hinta_euro):
    # Muutetaan halkaisija metreiksi
    halkaisija_m = halkaisija_cm / 100
    # Lasketaan säde
    sade = halkaisija_m / 2
    # Lasketaan pizzan pinta-ala (ympyrän ala)
    ala = math.pi * sade ** 2
    # Lasketaan yksikköhinta (€/m²)
    yksikkohinta = hinta_euro / ala
    return yksikkohinta

# Pääohjelma
def main():
    print("Anna ensimmäisen pizzan tiedot:")
    halkaisija1 = float(input("Halkaisija (cm): "))
    hinta1 = float(input("Hinta (€): "))

    print("\nAnna toisen pizzan tiedot:")
    halkaisija2 = float(input("Halkaisija (cm): "))
    hinta2 = float(input("Hinta (€): "))

    # Lasketaan yksikköhinnat funktiolla
    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    # Tulostetaan tulokset
    print(f"\nPizza 1: {yksikkohinta1:.2f} €/m²")
    print(f"Pizza 2: {yksikkohinta2:.2f} €/m²")

    # Verrataan kumpi on edullisempi
    if yksikkohinta1 < yksikkohinta2:
        print("\nEnsimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("\nToinen pizza antaa paremman vastineen rahalle.")
    else:
        print("\nPizzat ovat yhtä edullisia.")

# Käynnistetään pääohjelma
if __name__ == "__main__":
    main()
