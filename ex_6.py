#!/usr/bin/env python3
import json
import sys
# import os.path
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as Unique

# path = os.path.dirname(__file__) + "\\data_light_cp1251.json"
path = sys.argv[1]

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=lambda x: x.lower())


@print_result
def f2(arg):
    return list(filter(lambda x: (not x.lower().find("программист")), arg))


@print_result
def f3(arg):
    return list(map(lambda x: (x + " c опытом Python"), arg))


@print_result
def f4(arg):
    return list(zip(arg,
                    map(lambda x: ("зарплата " + str(x) + " руб."),
                        gen_random(100000, 200000, len(arg)))))


with timer():
    f4(f3(f2(f1(data))))
