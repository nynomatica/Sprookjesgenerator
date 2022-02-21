# todo make function for generating malename in dutch
from random import random, choice

from R import jongensnamen


def malename(name=''):
    # l = [['p','b','br', 'pr'], ['a', 'e', 'i', 'o', 'u','oe','ui'], ['l', 'm', 'nker','link','r']]
    # for g in l:
    #     name = name + choice(g)
    #return name
    return choice(jongensnamen)


