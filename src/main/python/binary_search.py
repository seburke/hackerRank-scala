

t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    #convert a to dict
    priceDict = {}
    for i in range(len(a)):
        if priceDict.has_key(a[i]):
            priceDict[a[i]].append(i+1)
        else:
            priceDict[a[i]] = [i+1]
    for k in priceDict.keys():
        if m - k in priceDict:
            if m - k == k and len(priceDict[k]) > 1:
                #have match
                indices = [str(x) for x in priceDict[k].sort()]
                print ' '.join(indices)
                break
            elif m - k != k:
                #have match
                indices = priceDict[k] + priceDict[m-k]
                indices = [str(x) for x in indices.sort()]
                print ' '.join(indices)
                break
