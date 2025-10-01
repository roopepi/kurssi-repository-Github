OIKEA_TUNNUS = "python"
OIKEA_SALASANA = "rules"
max_yritykset = 5
yritys = 0

while yritys < max_yritykset:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
    if tunnus == OIKEA_TUNNUS and salasana == OIKEA_SALASANA:
        print("Tervetuloa")
        break
    else:
        yritys += 1
        print(f"Väärä käyttäjätunnus tai salasana. Yrityksiä jäljellä: {max_yritykset - yritys}")

if yritys == max_yritykset:
    print("Pääsy evätty")
