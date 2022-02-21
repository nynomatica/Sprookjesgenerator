from woorden import vowelcount, countvowellist, isvowel

def maakverkleining(woord, ext=''):
    cv =  vowelcount(woord)
    if cv[-1] == 'm':
        ext = 'p'
    # if countvowellist(cv) < 2:
    #     return ''.join(cv) + cv[-1]+'e' + 'tje'

    return ''.join(cv) +ext+'je'

