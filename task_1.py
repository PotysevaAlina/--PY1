# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint


def number_systems(value):
    dicts_ = [dict([('bin', bin(i)), ('dec', i), ('hex', hex(i)), ('oct', oct(i))]) for i in range(value + 1)]
    return dicts_


pprint(number_systems(15))
