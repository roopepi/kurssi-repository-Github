# Vakioarvot
NAULAA_LEIVISKASSA = 20
LUOTIA_NAULASSA = 32
GRAMMAA_LUODISSA = 13.3

# Kysy syötteet
leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

# Laske kokonaisluodit
kokonaisluodit = leiviskat * NAULAA_LEIVISKASSA * LUOTIA_NAULASSA + naulat * LUOTIA_NAULASSA + luodit

# Muunna grammoiksi
kokonaisgrammat = kokonaisluodit * GRAMMAA_LUODISSA

# Erottele kilogrammat ja grammamäärä
kilogrammat = int(kokonaisgrammat // 1000)
grammat = kokonaisgrammat % 1000

# Tulosta tulos
print("Massa nykymittojen mukaan:")
print(kilogrammat, "kilogrammaa ja", grammat, "grammaa.")
