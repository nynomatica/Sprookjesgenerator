import random

import generators.CityNameRND
import generators.FemaleNameRND
# from context import cityname,citycount,citypopulation
from generators.CityNameRND import cityname
from wordmanipulations.captallist import capitallist
from wordmanipulations.uniquelist import uniquelist
import csv


class city:
    def __init__(self, world):
        l = []
        for i in range(world.citycount):
            l.append(generators.CityNameRND.cityname())
        l.sort()
        l = uniquelist(l)
        l = capitallist(l)
        world.cityname = l
        world.citycount = len(world.cityname)

        for i in range(world.citycount):

            rpos = random.randrange(len(world.HasCity))
            # situatie hier is dat er niet 2 steden op dezelfde cell mogen komen
            # ook wil ik hier een cell inplaats van een waarde true gebruiken
            while world.HasCity[rpos] == True:
                rpos = random.randrange(len(world.HasCity))
            world.HasCity[rpos] = True

            #  Todo populatie heeft hier een normaal verdeling verdeling moet anders namelijk minder grote steden
            #  basis is het om hier een random range te geven en tevreden te zijn met de normaal verdeling
            # daarna een functie te draaien met aantal en een multiplicator
            world.cityname.append(cityname())
            world.citypopulation.append(random.randrange(85, 300))
        # 10 maal meer bewoners hier is dus de controle voor grotere steden
        for i in range(int(world.citycount / 10)):
            j = random.randrange(world.citycount)
            world.citypopulation[j] = world.citypopulation[j] * 10

        for i in range(int(world.citycount / 100)):
            j = random.randrange(world.citycount)
            world.citypopulation[j] = world.citypopulation[j] * 30

        for i in range(int(world.citycount)):
            world.citypopulation[i] += random.randint(0,9)

    def savetocvs(self,fname,world):
        c = open(fname, 'w')
        o = csv.writer(c)
        for p in range(world.citycount):
            o.writerow(
                [ world.cityname[p],world.citypopulation[p] ])
        c.close()

        # with open(fname, 'w',
        #           newline='') as csv_file:  # open() function along with append mode "a"and newline=''
        #     write_csv = csv.writer(csv_file, delimiter=',')  # csv.writer() is used to write content in the CSV file
        #     write_csv.writerow()  # csv.writerow() to add a row and append the contentExecute the writing_into_csv.py script using Python,
        # # f = open(filename,"w")
        # for i in world.citycount:
        #     name = world.cityname[i]
        #     population =world.citypopulation[i]
        #     line = f"{name},{population}\n"
        #     f.write(self,line)
        #
        # f.close()



