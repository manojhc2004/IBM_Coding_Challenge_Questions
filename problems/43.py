"""Problem statement
You are given an array of N integers. Your task is to find the first element that occurs more than once when traversing the array from left to right.

If no element repeats, print -1.

Input format
- First line contains an integer N, representing the size of the array.
- Second line contains N space-separated integers.
Output format

Print the first repeating element. If no repeating element exists, print -1."""


def twice(nums):


    if len(nums) <=1:return -1
    hash = {}

    for num in nums:

        if num in hash:
            return num
        else:
            hash[num] = 1 
    
    return False




print(twice([1,2,3,4,5,6,1,9]))