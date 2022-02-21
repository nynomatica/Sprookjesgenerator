def uniquelist(alist):
    last =''
    out  =[]
    for item in alist:
        if item != last:
            out.append(item)
        last = item
    return out