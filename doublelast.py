from homogene import homogene
from woorden import vowelcount


def doublelast(woord):
    """
    zoiets als
    dik dikk
    maar niet gans gansns
    :param woord:
    :return:
    """
    l = vowelcount(woord)
    if len(l[-1])==1 and  homogene(l[-1]):
        l[-1] = l[-1] + l[-1]
    return ''.join(l)

