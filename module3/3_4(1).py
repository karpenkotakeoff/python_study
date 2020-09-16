# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A
# есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C
# можно перейти за один переход и из C в B можно перейти за один переход.
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на
# существующие HTML документы.

import requests
import re

list_url = []
list_url2 = []
a = input()
b = input()


def search_url(url, list_url):
    res = requests.get(url)
    text = res.text
    list_url += re.findall(r"<a\shref=\"(.+)\">\d</a>", text)


search_url(a, list_url)
for url in list_url:
    search_url(url, list_url2)
if b in list_url2:
    print("Yes")
else:
    print("No")
