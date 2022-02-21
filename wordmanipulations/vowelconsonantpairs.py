from woorden import isvowel


def vowelconsonantpairs(aword):
    """
    Grouping is the process of grouping consonants and vowels together in a list
    example :boom  -> ['b','oo','m']
             gans  -> ['g','a','ns']
     a group has either consonants or vowels
    :param aword:
    :return: list
    """
    buf = ''
    lout = []
    if aword != "":
        last = isvowel(aword[0])
    for i in aword:
        n = isvowel(i)
        if n != last:
            lout.append(buf)
            buf = ''
        last = n
        buf += i
    if buf != '':
        lout.append(buf)
    return lout