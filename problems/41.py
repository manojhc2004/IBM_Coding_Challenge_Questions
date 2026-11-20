"""Problem: Longest Subarray with Sum Divisible by K
Medium | Prefix Sum | HashMap
Problem Statement:

You are given an integer array arr of size n and an integer k.

Find the length of the longest contiguous subarray whose sum is divisible by k.

If no such subarray exists, return 0.

arr = [2, 7, 6, 1, 4, 5]
k = 3

output:
4"""



def longestsub(arr, k):

    
    maxx = 0
    summ = 0

    hashmap = {0: -1}

    for i in range(len(arr)):

        summ += arr[i]
        remaining = summ % k 

        
        if remaining in hashmap:
            maxx = max(maxx, i - hashmap[remaining])

            
        
        else:
            hashmap[remaining] = i 
        
    
    return maxx



print(longestsub([2, 7, 6, 1, 4, 5], 3))