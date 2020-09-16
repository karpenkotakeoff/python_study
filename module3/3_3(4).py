# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\".

import sys
import re

for line in sys.stdin:
    if re.search(r"\\", line):
        print(line.rstrip())