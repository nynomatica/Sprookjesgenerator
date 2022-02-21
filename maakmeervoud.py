from woorden import vowelcount, countvowellist, isvowel


def maakmeervoud(woord, ext='en'):
    # laatste letter xyz komen niet voor comment
    # laatste letter klinker dan en
    # laatste letter niet klinker en 1 klinker daarna dan copy laatste letter en en
    # laatste letter z dan z -> s en f dan v
    # geen letters dan ???
    # laatste letter consonant en compound vowel dan en

    # split eerst het woord in een lijst waarin klinkers en medeklinkers staan
    # c


    cv = vowelcount(woord)

    # laatste letter klinker dan ->


# aai aaien
    if len(cv)<2:
        return ''.join(cv)+'en'

#meervoud verklein woorden
# tonnetje tonnetjes zonnetje zonnetjes -> je jes
    if cv[-1]=='e' and cv[-2][-1]=='j':
        return  ''.join(cv)+'s'

# jongen jongens
    if cv[-1]=='n' and cv[-2]=='e':
        return  ''.join(cv)+'s'
    if (isvowel(cv[-1] ) == False) and  len(cv[-1]) > 1:
        if cv[-1][0] != cv[-1][1]:
            return ''.join(cv) + 'en'

    if isvowel(cv[-1] ) == isvowel(cv[-2]):
        cv.remove(last)
    if isvowel(cv[-1] ) == False:
        # en + mnp


        if cv[-1][-1] == 's':
            cv[-1] = 'z'
        if cv[-1]  == 'f':
            cv[-1] = 'v'

        if cv[-2] in ['o','a','i','u','e']:
            cv[-1] = cv[-1] * 2
        if cv[-2] in ['oo','aa','ee','uu']:
            cv[-2] = cv[-2][0]


        cv.append('en')
    return ''.join(cv)








