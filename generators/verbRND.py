# todo make function for generating malename in dutch
from random import random, choice

import R
from R import jongensnamen


def verbRND(name=''):
    # l = [['p','b','br', 'pr'], ['a', 'e', 'i', 'o', 'u','oe','ui'], ['l', 'm', 'nker','link','r']]
    # for g in l:
    #     name = name + choice(g)
    #return name
    return choice(R.werkwoorden)



