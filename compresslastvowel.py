from homogene import homogene
from woorden import isvowel, vowelcount


def compresslastvowel(woord):
    """
    bijvoorbeeld
    boom -> bom
    maar niet
    biek -> biek
    :param groups:
    """
    groups = vowelcount(woord)
    groups.reverse()

    for i in range(0,len(groups)):
        if isvowel(groups[i]):
            if len(groups[i])>1 and homogene(groups[i]):
                groups[i] = groups[i][0]
                groups.reverse()
                return ''.join(groups)
    groups.reverse()
    return  ''.join(groups)
