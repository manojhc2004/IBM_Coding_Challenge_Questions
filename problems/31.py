"""
Question 2: Equal 0s and 1s Subarray (Medium)

Problem Statement: Given a binary array (containing only 0s and 1s), find the maximum length of a contiguous subarray where the total count of 0s is exactly equal to the total count of 1s, with the added constraint that at any point within that prefix subarray, the count of 0s never exceeds the count of 1s.
• Example Input: [1, 0, 1, 1, 0, 0]
• Example Output: 6 (The entire array matches the criteria)"""



def binarycount(arr):

    output = 0
    hash = {1: 0, 0: 0}
    left = 0

    for i in range(len(arr)):

        hash[arr[i]] += 1

        while hash[0] > hash[1]:

            hash[arr[left]] -= 1
            left += 1

        if hash[0] == hash[1]:
            output = max(output, i - left + 1)

    return output


arr = [1, 1, 0, 0, 1, 0, 1, 0]
print(binarycount(arr))