import random
from random import randint


def randomwalk(base, steplow, stephigh, count):
    while count > 0:
        if random.random() > 0.5:
            base += randint(0,steplow)
        else:
            base -= randint(0,stephigh)
        count -=1
    return base

