# Posortować wyrazy z napisu line raz alfabetycznie, a raz pod
# względem długości. Wskazówka: funkcja wbudowana sorted().

import re

line = """Jakis napis wielowierszowy.
Kolejny wiersz tego napisu,
I jeszcze jeden"""

wiersz = re.split("\s+", line)

print("Posortowane alfabetycznie:", sorted(wiersz))
print("Posortowane pod wzgledem dlugosci:", sorted(wiersz, key=len))