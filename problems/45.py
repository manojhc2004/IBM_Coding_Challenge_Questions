"""Problem statement
A company stores transaction values in an integer array. You are given an array of N integers and a target value K.

Your task is to find the total number of pairs of elements whose sum is equal to K.

Each pair must contain elements from different indices.

Input format
- First line contains two integers N and K.
- Second line contains N space-separated integers.
Sample Input 1
6 6
1 5 7 -1 5 1"""


def cntpair(nums,k):


    hash = {}
    count = 0

    for num in nums:

        required = k - num

        if required in hash:
            count+= hash[required]
        
        hash[num] = hash.get(num, 0)+1
    
    return count


print(cntpair([2,2,2,2], 4))