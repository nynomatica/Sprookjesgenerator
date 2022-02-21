def homogene(s, last=None):
    last =str(s)[0]
    for i in s:
        if i!=last:
            return False
    return True

# for l in letters[::-1]:
#     print(l)