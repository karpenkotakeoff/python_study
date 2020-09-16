# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.

import sys
import re

for line in sys.stdin:
    if re.search(r"\bcat\b", line):
        print(line.rstrip())
