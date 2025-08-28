import math

def main():
    try:
        sade = float(input("Anna ympyrän säde: "))
        if sade < 0:
            print("Säde ei voi olla negatiivinen.")
            return
        pinta_ala = math.pi * sade ** 2
        print(f"Ympyrän pinta-ala on: {pinta_ala:.2f}")
    except ValueError:
        print("Virheellinen syöte. Anna numeerinen arvo.")

if __name__ == "__main__":
    main()
