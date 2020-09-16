# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого
# JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список
# имен прямых предков.
#
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Для каждого класса вычислите предком скольких классов он является и выведите эту
# информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

import json
struct = {}
res = {}
new = {}
inp = json.loads(input())
data = json.dumps(inp)
data_again = json.loads(data)


def dfs_recursive(graph, vertex, path):
    path += [vertex]
    for child in graph[vertex]:
        if child not in path:
            dfs_recursive(graph, child, path)
    return path


for i in range(len(inp)):
    struct[inp[i]["name"]] = inp[i]["parents"]
for key in struct:
    lis = []
    dfs_recursive(struct, key, lis)
    struct[key] = lis
for key in struct:
    res[key] = 0
    for value in struct.values():
        if key in value:
            res[key] += 1

# Вывод
for key, item in sorted(res.items()):
    print(str(key) + " : " + str(item))
