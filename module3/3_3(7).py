# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв
# "a" (регистр не важен), на слово "argh".

import sys
import re

for line in sys.stdin:
    print(re.sub(r"\b[aA]+\b", "argh", line, count=1).rstrip())
