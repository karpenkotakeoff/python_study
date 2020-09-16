# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.
# Пример:
# s = "abababa"
# t = "aba"
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa

s = input()
t = input()
n = 0
counter = 0
while n <= len(s) - (len(t)-1):
    i = s[n:n+len(t)]
    if i.find(t) == 0:
        counter += 1
    n += 1
print(counter)
