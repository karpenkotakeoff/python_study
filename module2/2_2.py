# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной
# даты date пройдет число дней, равное days.

import datetime

y, m, d = input().split()
addays = datetime.timedelta(days=int(input()))
now = datetime.date(int(y), int(m), int(d))
res = now + addays
print(str(res.year) + " " + str(res.month) + " " + str(res.day))
