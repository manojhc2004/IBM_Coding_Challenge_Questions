"""Next: Problem 9 – Move Zeroes
IBM-style practice
 Easy–Medium


Given an integer array, move all zeroes to the end while maintaining the relative order of non-zero elements.

Input:
7
0 1 0 3 12 0 5


Output:
1 3 12 5 0 0 0"""


def movezeros(arr):


    left = 0

    for right in range(len(arr)):

        if arr[right]!= 0:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
        
    
    return arr



print(movezeros([0,1,0,3,12,0,5]))