"""Given a sorted array of integers, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must place the result in the first part of the array. More formally, if there are K unique elements, then the first K elements of the array should hold the final result.
Your program should return the number of unique elements K.

📥 Input Format

• The first line contains an integer N, denoting the size of the array.
• The second line contains N space-separated integers, representing the elements of the sorted array.

📤 Output Format

• Print a single integer representing the count of unique elements (K).
• Print the first K elements of the modified array separated by spaces.

📋 Constraints

• 1 ≤ N ≤ 10⁵
• \(-10^9 \le A[i] \le 10^9\)
• The array is guaranteed to be sorted in non-decreasing order.
• Optimal Target: Time Complexity: O(N), Auxiliary Space: O(1) (Two-Pointer Technique).

🎯 Sample Cases


Sample Input 1

text
3
1 1 2
Use code with caution.

Sample Output 1

text
2
1 2
Use code with caution.

Explanation 1

The function should return K = 2, with the first two elements of the array being modified to 1 and 2 respectively. It does not matter what is left beyond the returned length."""


def sortarray(arr):


    hash = {}

    for i in arr:

        if (i not in hash):
            hash[i] = 1
        else:
            continue
    
    output = list(hash.keys())
    return output


print(sortarray([1, 1, 2]))