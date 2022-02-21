from venv.homogene import homogene
from woorden import vowelcount


def singlelast(woord):
    """
    zoiets als
    dikk -<dik
    boo -> bo
    maar niet gans gan
    :param woord:
    :return:
    """
    l = vowelcount(woord)
    if len(l[-1])>1 and  homogene(l[-1]):
        l[-1] = l[-1][0]
    return ''.join(l)
