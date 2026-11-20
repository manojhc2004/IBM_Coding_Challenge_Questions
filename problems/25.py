"""You are given an array with only 0 and 1. You have to return the length of the maximum subarray that satisfies the following 2 conditions:
1. No. of 0's and No. of 1's should be equal.
2. Prefix of the subarray should never have the No. of 0's more than No. of 1's. i.e. No. of 1's can be more than or equal to No. of 0's.

Example:

Input:

 arr = [1, 0, 1, 1, 0, 0, 1],
 arr = [0,1,0,1,1,0,1]
Output:

 6
As [1, 0, 1, 1, 0, 0] is the most longest valid answer."""


def maxsubarry(arr):


    maxx = 0
    N = 0
    curr = 0


    for i in range(len(arr)):

        prefix = 0
        
        for j in range(i,len(arr)):

            if (arr[j] == 1):
                prefix+=1
            else:
                prefix-=1

                if (prefix < 0):
                    break

                if (prefix == 0):
                    maxx = max(maxx, j - i + 1)
        
    
    return maxx
                


      



print(maxsubarry([1, 0, 1, 1, 0, 0]))