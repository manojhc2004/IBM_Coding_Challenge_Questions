"""Problem 12 – Search in a Sorted Array
IBM-style practice
Easy–Medium
Binary Search

Problem statement
You are given a sorted array of N integers and a target value K.

Your task is to find the index of K in the array. If K is not present, return -1.

Input format
- First line contains N and K.
- Second line contains N sorted integers.
Sample Input 1
6 10
2 4 6 8 10 12


Sample Output 1
4"""


def binarysearch(arr,k):


    low = 0
    high = len(arr)-1

    while low < high:

        mid = (low + high) // 2

        if arr[mid] == k:
            return mid 
        
        elif arr[mid] < k:
            low = mid + 1

        else:
   
         high = mid - 1

    return -1

print(binarysearch([2, 4, 6, 8, 10, 12], 10))