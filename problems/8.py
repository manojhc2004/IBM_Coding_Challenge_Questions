"""Given an array of integers arr and a positive integer K, find the maximum sum of any contiguous subarray of size K.

Sample Test Case

• Input Array: [2, 1, 5, 1, 3, 2]
• Subarray Size (K): 3
• Output: 9
• Explanation: The contiguous subarrays of size 3 are:
	• [2, 1, 5] → Sum = 8
	• [1, 5, 1] → Sum = 7
	• [5, 1, 3] → Sum = 9 (Maximum)
	• [1, 3, 2] → Sum = 6
"""


def maxsub(arr,k):

    
    # base sum
    maxx = sum(arr[0:k])

    index = 1
    for i in range(k,len(arr)):

        curr = arr[index:i+1]

        # edge case
        maxx = max(maxx,sum(curr)) 
        
        index+=1
    
    return maxx


if __name__ == "__main__":

    array = [2, 1, 3, 1, 3, 2]
    kth = 3

    call = maxsub(array,kth)
    print(call)