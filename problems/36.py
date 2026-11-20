"""
Problem Description: Find the Majority Element

Given an array of size N, find the majority element. The majority element is the element that appears more than ⌊N / 2⌋ times in the array.
You may assume that the majority element always exists in the input array.

📥 Input Format

• The first line contains an integer N, denoting the size of the array.
• The second line contains N space-separated integers, representing the elements of the array.

📤 Output Format

• Print a single integer representing the majority element.

📋 Constraints

• \(1 \le N \le 10^5\)
• \(-10^9 \le A[i] \le 10^9\)
• Optimal Target: Time Complexity: \(O(N)\), Auxiliary Space: \(O(1)\) (Boyer-Moore Voting Algorithm)

🎯 Sample Cases


Sample Input 1

text
3
3 2 3
Use code with caution.

Sample Output 1

text
3
Use code with caution.

Explanation 1

The size of the array is 3. The threshold is ⌊3 / 2⌋ = 1.
The element 3 appears 2 times, which is greater than 1. Therefore, 3 is the majority element."""



def majorityelement(n,arr):

    hash = {}
    target = n // 2

    for i in arr:
        
        if i in hash:
            hash[i]+=1
            if (hash[i] > target):
                return i
        else:
            hash[i] = 1
    
    return -1


print(majorityelement(3,[3,2,3]))