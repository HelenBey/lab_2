#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = ['a', 'A', 'a', 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 10, 10)

# Реализация задания 2
[print(i) for i in Unique(data1, ignore_case=True)]

print("_")

[print(i) for i in Unique(data1, ignore_case=False)]

print("_")

[print(i) for i in Unique(data2)]
