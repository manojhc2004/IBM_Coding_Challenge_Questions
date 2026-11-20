"""You are given Process, its timestamp, and its limit. You are to find the No. of Unstable processes and return it.

A process is considered Unstable if the process has atleast one increasing and atleast one decreasing limit according to the timestamps.

Timestamps are given in seconds.

Example:

Input:

    process = ["A", "B", "A", "C", "D", "A"]
    timestamp = [10, 25, 30, 35, 15, 20]
    limit = [20, 18, 10, 8, 30, 27]
Output:

    1
As Process "A" has 20->27->10, which has 1 increasing and 1 decreasing limit. Therefore, 1 is the answer."""



def unstablepro(process, timestamp, limit):

    res = []
    hash = {}


    for i in range(len(process)):

        if process[i] not in hash:
            hash[process[i]] = []
        
        
        hash[process[i]].append([timestamp[i],limit[i]])

        
    # now sort the array 

    for key in hash.keys():

        curr = sorted(hash[key])
        id = 0

      
        for i in range(len(curr)-1):

            if (curr[i][1] < curr[i+1][1]):
                id+=1
            
            if (curr[i][1] > curr[i+1][1]):
                id+=1
        
        if id == 2:
            res.append(key)
    

    
    return res

        



print(unstablepro(["A", "B", "A", "C", "D", "A"],[10, 25, 30, 35, 15, 20], [20, 18, 10, 8, 30, 27]))