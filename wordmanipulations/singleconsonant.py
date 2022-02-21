from wordmanipulations.isvowel import isvowel


def singleconsonant(letters):
    last=''
    out = ''
    for i in letters:
        if isvowel(i) == False and last == i:
            i=''
        else:
            last=i
        out = out + i
    return out

