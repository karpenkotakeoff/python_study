# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

import sys
import re

for line in sys.stdin:
    if re.search(r"z...z", line):
        print(line.rstrip())
