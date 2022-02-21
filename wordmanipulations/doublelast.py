from venv.homogene import homogene
from woorden import vowelcount


def doublelast(l):
    """
    wil check if the last item in the list has one letter and will duplicate is so
    ['d','i','k'] -> ['d','i','kk']
    """
    if len(l[-1])==1 and  homogene(l[-1]):
        l[-1] = l[-1] + l[-1]
    return l

