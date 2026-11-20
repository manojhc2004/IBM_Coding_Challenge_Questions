"""
Maximum Subarray Sum
Easy–Medium
 Important DSA pattern


Problem statement:

Given an integer array, find the maximum possible sum of a contiguous subarray.

Input:
6
-2 1 -3 4 -1 2


Expected output:
5


Explanation:

The maximum-sum subarray is:
[4, -1, 2]

Sum = 4 - 1 + 2 = 5"""


def maxsubc(arr):



    # kadan's algorithm 

    currsum = arr[0]
    maxsum = arr[0]

    for i in range(len(arr)):

        # kadan's formula
        currsum = max(arr[i],currsum + arr[i])
        maxsum = max(maxsum, currsum)
    
    return maxsum


    

    
print(maxsubc([-2, 1, -3, 4, -1, 2]))