# Kysytään käyttäjältä sukupuoli ja hemoglobiiniarvo
sukupuoli = input("Anna biologinen sukupuolesi (mies/nainen): ").lower()
try:
    hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))

    if sukupuoli == "nainen":
        if hemoglobiini < 117:
            print("Hemoglobiiniarvo on alhainen.")
        elif hemoglobiini <= 175:
            print("Hemoglobiiniarvo on normaali.")
        else:
            print("Hemoglobiiniarvo on korkea.")
    elif sukupuoli == "mies":
        if hemoglobiini < 134:
            print("Hemoglobiiniarvo on alhainen.")
        elif hemoglobiini <= 195:
            print("Hemoglobiiniarvo on normaali.")
        else:
            print("Hemoglobiiniarvo on korkea.")
    else:
        print("Virheellinen sukupuoli.")
except ValueError:
    print("Virheellinen hemoglobiiniarvo. Anna arvo kokonaislukuna.")
