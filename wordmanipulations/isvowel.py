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
