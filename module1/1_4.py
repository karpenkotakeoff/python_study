# Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать
# поддержку создания пространств имен и добавление в них переменных.
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
# Вашей программе на вход подаются следующие запросы:
# - create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри
# - пространства <parent>
# - add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# - get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не существует
# В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global.
# Далее мы объявляем функцию foo, что влечет за собой создание локального для нее пространства имен
# внутри пространства global. В нашем случае, это описывается командой create foo global. Далее мы
# объявляем внутри функции foo функцию bar, тем самым создавая пространство bar внутри пространства foo,
# и добавляем в bar переменную a.
# Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
# Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена
# переменная a, но в пространстве global, внутри которого находится пространство foo, она объявлена.
# Аналогично, результатом запроса get bar b будет являться foo, а результатом работы get bar a будет
# являться bar.
# Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем
# пространстве global не была объявлена переменная с.
# Более формально, результатом работы get <namespace> <var> является
# - <namespace>, если в пространстве <namespace> была объявлена переменная <var>
# - get <parent> <var> – результат запроса к пространству, внутри которого было создано
# пространство <namespace>, если переменная не была объявлена
# - None, если не существует <parent>, т. е. <namespace> – это global

d = {"global": []}
res = []


def create(namespace, parent):
    d[namespace] = [parent]


def add(namespace, x):
    d[namespace].append(x)


def get(namespace, x):
    if namespace not in d:
        return None
    while True:
        if x in d[namespace]:
            return namespace
        else:
            if namespace == "global":
                return None
            namespace = d[namespace][0]


n = int(input())
while n > 0:
    cmnd, namespace, x = input().split()
    if cmnd == "create":
        create(namespace, x)
    elif cmnd == "add":
        add(namespace, x)
    elif cmnd == "get":
        a = get(namespace, x)
        res.append(a)
    n -= 1
for i in res:
    print(i)
