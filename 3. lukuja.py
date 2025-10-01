luvut = []

while True:
    syote = input("Anna luku (tai paina Enter lopettaaksesi): ")
    if syote == "":
        break  # Lopetetaan, jos syöte on tyhjä
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Virhe: Syötä kelvollinen numero!")

if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et antanut yhtään lukua.")
