# SprookjesGenerator Using English here. Hi i'm ray koster and i use this project as a way to learn python you are
# free to join and improve the code Goal is it to create a AI that is capable of generating fairytales in the dutch
# language. Currently the project is in it's very early stages. But be aware everything can and probably will change
# in later versions.
#
# First thing to do here is it to write the functions that will modify the stems of words.
# adding resources ?? what's the proper way
# learning TDD test driven development
# learning Pycharm
# learing Python

# Why this is public I know that a project like this should be private but the idea is just to good not to share.
# Also i'm searching for people that want to improve on the idea of this project. I'm not a programmer and have zero
# knowledge of programming and am bound to make mistakes. So any constructive critique is welcome. For the rest have
# fun !
import random
from random import choice

import globalevent
from generators.CityNameRND import cityname
from generators.FemaleNameRND import femalernd
from generators.MaleNameRND import malename

from generators.randomword import randomword
from generators.verbRND import verbRND
from maakmeervoud import maakmeervoud
from woorden import vowelcount
from wordmanipulations.captallist import capitallist
from wordmanipulations.plural import plural
from wordmanipulations.uniquelist import uniquelist
from wordmanipulations.vowelconsonantpairs import vowelconsonantpairs


def print_hi(name): # Todo remove this
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    event = globalevent.globalEvent() # Todo remove this
    count = vowelcount("oeluuluilkfm") # Todo remove this
    maakmeervoud('test') # Todo remove this
    if ['a', 'b', 'c'] == ['a', 'b', 'c']: # Todo remove this
        print("is true")

    print(f"{count}")  # todo remove this
    print_hi(f'PyCharm \n\nResponse : {event.text()}') # todo remove this
    # main demo for now
    print("SprookjesGenerator")
    print("")
    print("fase 0 : making functions for manipulating words")
    print("fase 1 : tokenize sentences")
    print("fase 2 : making generators")
    print(randomword(10))

    l = []
    print("Random female names (old dutch)")

    for i in range(2000):
        #print(verbRND())
        #print(femalernd())
        # l.append(cityname())
        l.append(femalernd())
    l.sort()
    l = uniquelist(l)
    l = capitallist(l)
    print(l)
    print(len(l))

    print("-------------------------------------------------------------")
    l = []
    print("Random city names (old dutch)")
    for i in range(2000):
        #print(verbRND())
        #print(femalernd())
        # l.append(cityname())
        l.append(cityname())
    l.sort()
    l = uniquelist(l)
    l = capitallist(l)
    print(l)
    print(len(l))
    print("-------------------------------------------------------------")
    print("So to put is all together it becomes something like")
    random.seed(11)
    stad = cityname().capitalize()
    meisje = femalernd().capitalize() +' '+malename()+'sdochter'
    time = choice(["morgen","volgende week","vandaag","volgende maand"])
    print("")
    print(f"{meisje} gaat {time} naar {stad}.")

    # print(plural(vowelconsonantpairs('boom')))
    # print(R.zelfstandigenaamwoorden)