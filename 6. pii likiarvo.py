import random

def laske_pii(pisteiden_maara):
    n = 0  # ympyrän sisälle osuneiden pisteiden lukumäärä

    for _ in range(pisteiden_maara):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            n += 1

    pii = 4 * n / pisteiden_maara
    return pii

def main():
    try:
        pisteiden_maara = int(input("Anna arvottavien pisteiden määrä: "))
        if pisteiden_maara <= 0:
            print("Anna positiivinen kokonaisluku.")
            return
    except ValueError:
        print("Virheellinen syöte, anna kokonaisluku.")
        return

    likiarvo = laske_pii(pisteiden_maara)
    print(f"Piin likiarvo arvottavilla pisteillä: {likiarvo}")

if __name__ == "__main__":
    main()
