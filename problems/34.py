"""
Problem Statement: Move All Zeroes to the End

Given an unsorted integer array arr[] of size N, write a function to move all the 0s in the array to the end. You must do this in-place without making a copy of the array (no extra array allowed).
Crucially, you must maintain the relative order of all the non-zero elements. For example, if 5 appeared before 3 in the original array, 5 must still appear before 3 after the zeroes are moved.

Example 1

• Input:
	• N = 5
	• arr[] = [0, 1, 0, 3, 12]  [1,0,0,3,12] [1,3,0,0,12] [1,3,12,0,0,0]
• Output:
	• arr[] = [1, 3, 12, 0, 0]

• Explanation: The non-zero elements 1, 3, and 12 keep their original order, while both 0s are pushed to the back.

Example 2

• Input:
	• N = 4
	• arr[] = [0, 0, 0, 4]    [0,0,0,4] [4,0,0,0]
• Output:
	• arr[] = [4, 0, 0, 0]
    arr [] = [3,1,0,5,0,4]
"""


def movezeros(N, arr):


    swap = 0


    for i in range(len(arr)):

        if (arr[i] !=0):
            arr[swap],arr[i] = arr[i],arr[swap]
            swap+=1
        
    return arr 


    


print(movezeros(5,[1,2,0,3,0]))