"""two sum using hashmap"""



def twosum(num,k):


    hash = {}

    for i in range(len(num)):

        if (k - i in hash):
            return [hash[k-i],i]
        
        hash[num[i]] = i


print(twosum([1,2,3,4,5],3))