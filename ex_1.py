#!/usr/bin/env python3
from librip.gens import field
from librip.gens import gen_random
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]
# Реализация задания 1
a = [1, 2, 3, 4, 5]

print(type(a))

[print('|', i, '|', end=" ") for i in field(goods, 'title')]

print()

[print('|', i, '|', end=" ") for i in field(goods, 'title', 'color')]

print()

[print('|', i, '|', end=" ") for i in gen_random(1, 3, 5)]