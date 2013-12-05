string = 'ambohimanga is a hill and traditional fortified royal sellement'
sl = list(string)
seen = {}
for i in range(0, len(list(string))):
    if sl[i] in seen:
        del sl[i]
    else:
        seen[sl[i]] = True

print ''.join(sl)