# Лямбда функции предоставляют нам удобный способ создать функцию «прямо на месте».
# Но иногда, когда нужно создавать много однотипных лямбда функций, еще удобнее будет
# создать функцию, которая будет их генерировать.
# Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию
# от одного аргумента y, которая будет возвращать True, если остаток от деления y на x равен
# mod, и False иначе.

def mod_checker(x, mod=0):
    return lambda y: y % x == mod

# mod_checker = lambda y, mod=0: lambda x: x % y == mod
