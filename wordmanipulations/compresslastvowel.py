def compresslastvowel(group):
    """
    will compress the lastvowelgroup is homogene and len>1
    example :
    boom -> bom
    but not
    biek -> biek
    :param groups:
    """
    groups = group
    groups.reverse()

    for i in range(0,len(groups)):
        if isvowel(groups[i]):
            if len(groups[i])>1 and homogene(groups[i]):
                groups[i] = groups[i][0]
                groups.reverse()
                return groups
    groups.reverse()
    return groups