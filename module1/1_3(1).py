# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного
# аргумента целое число x и возвращающую самое маленькое целое число y, такое что:
# - y больше или равно x
# - y делится нацело на 5

from math import ceil
def closest_mod_5(x):
    res = ceil(x/5)*5
    return res