def capitallist(alist):
    out = []
    for item in alist:
        s = str(item)
        s = s.capitalize()
        out.append(s)
    return out
