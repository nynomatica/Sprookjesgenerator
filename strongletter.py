def strongletter(woord):
    """
    zoiets als
    slaaf
    slaven
    baas
    baaz
    :param woord:
    :return:
    """
    letters=list(woord)
    if letters[-1] == 's':
        letters[-1] = 'z'
    if letters[-1] == 'f':
        letters[-1] ='v'
    return ''.join(letters)



