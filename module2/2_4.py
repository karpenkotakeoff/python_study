# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

lis = []
with open("dataset_24465_2-4.txt", "r") as r, open("output.txt", "w") as w:
    for line in r:
        lis.append(line)
    lis.reverse()
    for i in lis:
        w.write(i)
