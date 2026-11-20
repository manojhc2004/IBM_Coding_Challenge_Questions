"""Given an integer array load (of length n) representing server loads at different timestamps, find all 0-based indices where the load value is greater than twice the average load. Return the results in increasing order; if no such indices exist, return an empty array.

Example

Input: n=3, load=[1,2,9]

Calculation: Average load = (1+2+9)/3 = 4; twice the average load = 8. Only the load at index 2 (value 9) is greater than 8.

Output: [2]"""


def loadbalance(n, load): #parameters

    # edge case!
    if (n == 0):
        return [] # zero cannot be divisible

    avg = sum(load) // n 
    twice = avg * 2

    for i in range(len(load)):

        if (load[i] > twice):
            return i
    
    return []


print(loadbalance(3, [1,2,9]))