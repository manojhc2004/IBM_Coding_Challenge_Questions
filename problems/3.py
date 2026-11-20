"""There are numItems items (numbered from 0 to numItems-1), and each item may have multiple cost options. Given two arrays itemId (length n, each element is an item number) and cost (length n, the corresponding cost for each item number), select exactly one cost option for each item and find the minimum total cost. If any item has no cost options, return -1.

Example

Input: numItems=3, n=4, itemId=[2,0,1,2], cost=[8,7,6,9]

Analysis: The minimum cost for item 0 is 7, for item 1 is 6, and for item 2 is 8 (choosing the smaller value between 8 and 9).

Output: 7+6+8=  21 """

noitems = 3
N = 4
Id =    [2,0,1,2]
value = [8,7,6,9]


def mincost(numItems,n, itemid, cost): # parameters


    hm = {}

    
    for i,j in zip(itemid, cost):

        if (i in hm):

            if (hm[i] > j):
                hm[i] = j
        else:
            hm[i] = j

    # edge case 
    if (len(hm) != numItems):
        return -1

    res = sum(hm.values())
    return res


print(mincost(noitems,N,Id,value))