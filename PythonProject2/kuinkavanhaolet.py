pituus = int(input("anna pituutesi: "))
paino = int(input("anna painosi: "))

#muuttuja jossa lasku suoritetaan
bmi = paino / (pituus / 100) ** 2

print("pituus-paino-indeksisi on", bmi)

