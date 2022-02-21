from wordmanipulations.isvowel import isvowel


def maxconsonant(letters):
    seq = 0
    mx = 0
    for letter in letters:
        if isvowel(letter)==False:
            seq +=1
        else:
            seq = 0
        if seq > mx:
            mx = seq
    return mx
