# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

import re

line = """Jakis napis wielowierszowy.
Kolejny wiersz tego napisu,
I jeszcze jeden"""

wiersz = re.split("\s+", line)

najdluzszy = 0

for element in wiersz:
    if len(list(element)) > najdluzszy:
        najdluzszy = len(list(element))
        najdluzszy_wyraz = element

print("Najdluzszy wyraz: " + najdluzszy_wyraz)
print("Dlugosc najdluzszego wyrazu:", najdluzszy)