import random

class Man_valt:
    @staticmethod
    def generate():
        person = random.choice(["Man","Vrouw"])
        return f"{person} valt"

class Man_gaat:
    def generate(self):
        person = random.choice(["Man","Vrouw"])
        return f"{person} gaat"

class Man_verlaat:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} verlaat"

class Man_sterft:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} sterft"

class Man_trouwt:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} trouwt"

class Man_slaat:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} slaat"

class Man_aangevallen:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} aangevallen"

class Man_gaat_naar:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} gaat naar"

class Man_is_vermist:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} is vermist"


class Man_steelt:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} steelt"


class Man_geeft:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} geeft"


class Man_geexecuteerd:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} geexecuteerd"


class Man_verdrinkt:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} verdrinkt"


class Man_vind:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} vind"


class Man_ontmoet:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} ontmoet"

class Man_ziek:
    def generate(self):
        person = random.choice(["Man", "Vrouw"])
        return f"{person} ziek"


class Er_is_honger:
    def generate(self):
        return "Er is honger"

class Er_is_oorlog:
    def generate(self):
        return "Er is oorlog"

class Er_is_ziekte:
    def generate(self):
        return "Er is ziekte"


class Er_is_armoede:
    def generate(self):
        return "Er is armoede"

#
# • Man verdrinkt
# • Man vind
# • Man ontmoet
# • Man ziek
# • Man word rijk
# • Er is Oorlog
# • Er is honger
# • Er is ziekte
# • Er is armoede

class globalEvent:
    def text(self):
        """
dit zijn dus een aantal basis generators die een of meer basis zinnen genereren
een soort nieuwsbericht. zoals v.b. de 14 jarige blondharige zoon van bakker tekelman is gisteravond omstreeks 4 uur in de korenbloemstraat op zijn hoofd gevallen -> man valt
daar naar man valt  effect de kleine jongen is zwaargewond naar het ziekenhuis gebracht waar weetmeester grinderwald hem medisch onderzocht heeft.

        :return:
        """
        l=[Man_valt,Man_gaat,Man_verlaat,Man_sterft,Man_trouwt,Man_slaat,Man_aangevallen,Man_gaat_naar,Man_is_vermist,
           Man_steelt,Man_geeft,Man_geexecuteerd,Man_verdrinkt,Man_vind,Man_ontmoet,Man_ziek,Er_is_honger,Er_is_oorlog,
           Er_is_ziekte,Er_is_armoede]

        chosen = random.choice(l)
        return chosen().generate()


        # return "UH???"

