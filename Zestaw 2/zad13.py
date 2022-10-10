# Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().

import re

line = """Jakis napis wielowierszowy.
Kolejny wiersz tego napisu,
I jeszcze jeden"""

suma = 0

wiersz = re.split("\s+", line)
for element in wiersz:
    suma += len(list(element))

print(suma)