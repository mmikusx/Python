# W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

import re

line = """Jakis napis GvR wielowierszowy.
Kolejny wiersz tego napisu,
I jeszcze jeden GvR"""

print("Przed zmiana: \n" + line +"\n")

print("Po zmianie: \n" + line.replace("GvR", "Guido van Rossum"))