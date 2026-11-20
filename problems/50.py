id = [1,2,3,1,4,2,3,4]
l = [18,23,12,16,13,8,11,16]
kth = 3

def cummulative(ids,loads, k):

    res = []
    hash = {}

    for i in range(len(ids)):

        if ids[i] in hash:
            hash[ids[i]]+= loads[i]
        else:
            hash[ids[i]] = loads[i]


    val = list(reversed(sorted(set(hash.values()))))
    indx = 0

    while indx < k:

        for key in hash.keys():

            if val[indx] == hash[key]:
                res.append(key)
                break
        indx+=1


    return res


print(cummulative(id,l,kth))