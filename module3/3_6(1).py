# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли
# интересный математический факт об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

import requests

with open('dataset_24476_3-6.txt') as f:
    read = f.read().splitlines()

for x in read:
    res = requests.get(f'http://numbersapi.com/{x}/math?json=true')
    if res.json()['found']:
        print('Interesting')
    else:
        print('Boring')
