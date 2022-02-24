# SprookjesGenerator Using English here. Hi i'm ray koster and i use this project as a way to learn python you are
# free to join and improve the code Goal is it to create a AI that is capable of generating fairytales in the dutch
# language. Currently the project is in it's very early stages. But be aware everything can and probably will change
# in later versions.
#
# First thing to do here is it to write the functions that will modify the stems of words.
# adding resources ?? what's the proper way
# learning TDD test driven development
# learning Pycharm
# DO NOT RUN THIS IS STILL TOO EARLY FOR ANY RESULTS
# Why this is public I know that a project like this should be private but the idea is just to good not to share.
# Also i'm searching for people that want to improve on the idea of this project. I'm not a programmer and have zero
# knowledge of programming and am bound to make mistakes. So any constructive critique is welcome. For the rest have
# fun !
import random

from MaleNameRND import malename
from character import character
from city import city
from generators.FamilyNameRND import familynamernd
from world import world


class myApp():
    def run(self):
        # for i in range(100):
        #     print(malename())

        self.world =  world()
        city(self.world)
        character(self.world)
        # print(self.world.citypopulation)
        # print(self.world.cityname)
        # print(self.world.charactername)
        # print(self.world.charactersex)
        # print(self.world.characterfamilyname)

        # character.savetocvs(self,'/home/ray/Desktop/characters.csv',self.world)
        # , self.world)

        Sum = self.world.totalpopulation()
        print(f"Total population {Sum}")
        city.savetocvs(city,'/home/ray/Desktop/steden.csv',self.world)



if __name__ == '__main__':
    myApp().run()
    #world()
    #worldgen()
    #citygen()
    #print(generators.worldgen.citycount)


