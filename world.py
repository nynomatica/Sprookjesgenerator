class world():
    size = 0
    #  map die aangeeft dat op een tile een city staat
    HasCity = []
    citycount = 0
    citypopulation = []
    cityname = []

    # list of characters in world
    charactercount = 0
    character = []
    charactername = []
    charactersex = []
    characterfamilyname = []
    characterposition = []
    characteriq = []
    characteroogkleur = []
    characterlengte = []

    characterhaarkleur = []
    haar_kleur_type = ['blond'] * 5 + ['bruin']*10+['zwart']*5 +['rood']*2

    ogen_type = ["bruin"]*10 +["zwart"]*5+["blauw"]*3+["groen"]*2+["grijs"]
    ogen_tint = ['donker']+['licht']

    def __init__(self, aworldmapsize=10000, acitycount=1200,acharactercount =3000):
        """
        :param aworldmapsize:
        :param acitycount:
        """
        self.charactercount = acharactercount
        self.character = []
        self.size = aworldmapsize
        self.HasCity = [False] * self.size
        # Stads/Dorp definitie
        self.citycount = acitycount
        self.citypopulation = []
        self.cityname = ['']

    def totalpopulation(self, s=0):
        for i in range(self.citycount):
            s = s + self.citypopulation[i]
        return s

    def populationindex(self, idx):
        s = 0
        for i in range(self.citycount):
            s = s + self.citypopulation[i]
            if idx<s:
                return i-1

