# Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. Przez wyraz rozumiemy ciąg
# "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

import re

line = """Jakis napis wielowierszowy.
Kolejny wiersz tego napisu,
I jeszcze jeden"""

print(len(re.split("\s+", line)))
