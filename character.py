# makes a character
import csv
import random
from random import choice, randint

from functions import randomwalk
from generators.FamilyNameRND import familynamernd
from generators.FemaleNameRND import femalernd
from MaleNameRND import malename
from functions.randomwalk import randomwalk
import kivy



class character():
    def __init__(self, world):

        self.world = world
        totalpopulation = self.world.totalpopulation()
        for i in range(world.charactercount):
            sex = choice(["M","F"])
            self.world.character = sex
            if sex =="M":
                self.world.charactername.append(malename())
            else:
                self.world.charactername.append(femalernd())
            self.world.charactersex.append(sex)
            # position en achternaam

            # simpel verhaal hier achter naam is een stad bereken hier total population en randint over de population
            # TODO : uitbreiding is dat er meer variatie in achternamen moet komen
            idx = self.world.populationindex(randint(0,totalpopulation))
            if random.randint(0, 100) > 90:
                self.world.characterfamilyname.append('van '+world.cityname[idx])
            else:
                self.world.characterfamilyname.append(familynamernd())


            self.world.characterposition = idx

            # intelligentie ? maak hier een poging om eigenschappen toe te voegen
            iq = randomwalk(100,5,5,10)
            self.world.characteriq.append(iq)

            # oogkleur
            self.world.characteroogkleur.append(choice(self.world.ogen_type))

            # lichaamslengte
            body_length = randomwalk(170, 3, 3, 20)
            # is
            if sex == "F":
                body_length -= random.randint(3,10)
            self.world.characterlengte.append(body_length)

            # haarkleur
            self.world.characterhaarkleur.append(choice(self.world.haar_kleur_type))


    def savetocvs(self,fname,world):
            c = open(fname, 'w')
            o = csv.writer(c)
            for p in range(world.charactercount):
                o.writerow(
                    [ world.charactername[p].title(),
                      world.characterfamilyname[p].title(),
                      world.charactersex[p],
                      world.characteriq[p],
                      world.characteroogkleur[p],
                      world.characterlengte[p],
                      world.characterhaarkleur[p]
                      ])
            c.close()
