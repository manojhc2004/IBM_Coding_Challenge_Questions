"""
Problem Statement: Find the Missing Number

Given an unsorted array arr[] of size N - 1 containing distinct integers. The elements in the array are in the range of 1 to N. This means exactly one integer from the sequence of 1 to N is missing. Your task is to find and return that missing number.

Constraints

• \(1 \le N \le 10^6\)
• \(1 \le arr[i] \le N\)
• All elements in arr[] are distinct.
• Expected Time Complexity: \(O(N)\)
• Expected Auxiliary Space: \(O(1)\) (No hash sets or extra frequency arrays allowed)

Sample Inputs & Outputs


Example 1

• Input:
	• N = 5
	• arr[] = [1, 2, 4, 5]
• Output:
	• 3
• Explanation: The range is 1 to 5. The number 3 is missing from the array.

Example 2

• Input:
	• N = 3
	• arr[] = [1, 3]
• Output:
	• 2
• Explanation: The range is 1 to 3. The number 2 is missing.
"""


def missingnum(N, arr):


    
    missingsum = sum(arr)
    actualsum = 0

    for i in range(1, N+1):
        actualsum+=i 
    
    
    return actualsum - missingsum





print(missingnum(7,[1,2,4,3,5,7]))