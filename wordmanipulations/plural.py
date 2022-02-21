from compresslastvowel import compresslastvowel
from wordmanipulations.strongletter import strongletter
from wordmanipulations.vowelconsonantpairs import vowelconsonantpairs


def plural(vowelconsonantpair:list):

    vcp = vowelconsonantpair
    # jas jassen
    # boom bomen
    vcp = compresslastvowel(vcp) +'en'
    # vcp.append('e')
    # vcp.append('n') # todo error adding en impossible whyiio
    return vcp

def pluralword(letters):
    letters = strongletter(letters) # makes last letter strong

    return ''.join(plural(vowelconsonantpairs(list(letters))))
