import random
import string


def randomword(count=10):
    word = ''
    random.seed(2804)
    for i in range(0,count):
        randomLetter: string = random.choice(string.ascii_lowercase)
        word = word + randomLetter
    return word


