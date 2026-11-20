"""Problem 8 – Remove Duplicates From Sorted Array
IBM-style practice
Easy–Medium
Two Pointers

Problem statement
You are given a sorted integer array containing duplicate elements.

Your task is to remove the duplicate elements in-place such that each unique element appears only once.

Return the number of unique elements.

Input format
- First line contains integer N.
- Second line contains N sorted integers.
Sample Input 1
7
1 1 2 2 3 3 4


Sample Output 1
4"""


def rmvduplicate(arr):


    i = 0

    for j in range(len(arr)):

        if arr[j] != arr[i]:
            i+=1
            arr[i] = arr[j]
    
    return arr

print(rmvduplicate([1, 1, 2, 2, 3, 3, 4]))