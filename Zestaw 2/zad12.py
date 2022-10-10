# Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.

line = """Jakis napis wielowierszowy.
Kolejny wiersz tego napisu,
I jeszcze jeden"""

oddzielone_wiersze = line.split("\n")

z_pierwszych_liter = ''
z_ostatnich_liter = ''

for wiersz in oddzielone_wiersze:
    for wyraz in wiersz.split():
        z_pierwszych_liter += wyraz[0]
        z_ostatnich_liter += wyraz[-1]

print("Napis stworzony z pierwszych liter wyrazow: " + z_pierwszych_liter)
print("Napis stworzony z ostatnich liter wyrazow: " + z_ostatnich_liter)
