# todo make function for generating malename in dutch
# from random import random, choice
#
import random

from R import jongensnamen
from generators.FamilyNameRND import familynamernd


def malename(name=''):
    if random.randint(0, 100) > 70:
        return familynamernd()
    else:
        return random.choice(jongensnamen)
