vowels = ['a', 'e', 'i', 'o', 'u']

def isvowel(ch):
    """
        looks wether group is avowel or not
    :param ch:
    :return:
    """
    if ch == '':
        return True
    else:
        return ch[0] in vowels

def countvowellist(aword, count=0):
    alist = vowelcount(aword)
    for i in alist:
        if isvowel(i):
            count += 1
    return count



def vowelcount(aword):
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


def randomletters(count):
    pass



#randomletters(count)



