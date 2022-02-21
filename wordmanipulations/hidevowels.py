from wordmanipulations.isvowel import isvowel


def hidevowels(letters, out=''):
    for letter in letters:
        if isvowel(letter):
            out = out + '.'
        else:
            out = out + letter
    return out


