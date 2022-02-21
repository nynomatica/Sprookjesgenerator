#todo make function for generating cityname in dutch

# 1='a|e|i|o|u|oo|aa|oo|ee|oe|ui|ar|ij|oer|are,wegge|weg|ker|tten|tte|selo|sel|ster|st|mmen|ssen|rts|pert|l|chter|cht|mme|kel|k|kke|lst|lle|melo|ter';
#   _2='j|h|b|br|d|dr|g|j||k|kr|kl|l|m|n|p|pr|r|s|sl|sch|sm|t|tr|v|w|z|zw,aa|a|e|i|o|u|oe|ui,weg|wegge|ker|kke|lke|lkke|lst|l|melo|tter|lle|cht|chter';
#   _post='q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|dam|dam|dam|dam|veld|veld|velde|dorp|dorp|dorp|dorp|gat|gat|gat|gat|gat|stad|stad|stad|stad|dijk|hekse|trol|broek|broeke|huizen|huizen|brug|brug|brugge|berg|berg|berg|berg|donk|reus|bos|bos|bos|struik|struik|stoof|stoof|steen|geest|geest';
#   _pre='q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|q|hoog|klein|groot|boven|neder|laag|';

from random import random, choice, uniform


def cityname(name=''):
    numbers=['ander','wees','ieder','een','twee','drie','vier','vijf','zes','zeven','acht','negen','tien','elf','twaalf','dertien','veertien','vijftien','zestien','zeventien','achtien','negentien','twintig']

    _1 =['a','e','i','o','u','oo','aa','oo','ee','oe','ui','ar','ij','oer','are','pij']
    _2=['wegge','weg','ker','tten','tte','selo','sel','ster','st','mmen','ssen','rts','pert','l','chter','cht','mme','kel','k','kke','lst','lle','melo','ter']
    _post=['dam','dam','dam','dam','veld','veld','velde','dorp','dorp','dorp','dorp','gat','gat','gat','gat','gat',
           'stad','stad','stad','stad','dijk','hekse','trol','broek','broeke','huizen','huizen','brug','brug','brugge',
           'berg','berg','berg','berg','donk','reus','bos','bos','bos','struik','struik','stoof','stoof','steen','geest','geest','reus','reus',
           'veen','veen','veen','veen','meer','meer','meer','meer','vecht','vecht','vecht','bos','bos','bos','bos','bos','akker','akker','akker','bij den gat',' bij het bos',' bij de rivier'
           ]
    _pre=['hoog','klein','groot','boven','neder','laag']
    _dir=['oost','west','noord','zuid']

    if uniform(0,1)>0.8:
        Prefix =choice(_pre)
    else:
        Prefix =''

    if uniform(0,1)>0.8:
        Postfix =choice(_post)
    else:
        Postfix=''

    if uniform(0,1)>0.95:
        direction= choice(_dir)+' '
    else:
        direction=''

    if uniform(0,1)>0.1:
        out = direction+Prefix+choice(_1)+choice(_2)+Postfix
    else:
        out = choice(numbers)+'huizen'
    return out

