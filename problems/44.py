"""Problem statement
A company maintains a list of employee identification numbers. Some identification numbers may appear multiple times due to duplicate entries.

You are given an array of N integers. Your task is to calculate and print the frequency of each distinct element in the order in which each element first appears.

Input format
- First line contains integer N.
- Second line contains N space-separated integers.
Output format

Print each distinct element followed by its frequency.
Sample Input
7
10 20 10 30 20 10 40"""



def freqcount(nums):


    hash = {}

    for num in nums:

        if num in hash:
            hash[num]+=1
        else:hash[num] = 1


    for  key,val in hash.items():
        print(key,val)
        
    

print(freqcount([5, 2, 5, 8, 2, 5, 9, 8, 8, 1, 2, 5]))