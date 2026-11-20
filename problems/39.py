"""
📝 Problem Description: Find the Kth Smallest and Largest Element

Given an unsorted array of integers and an integer K, find both the Kth smallest and Kth largest elements in the array.
Note that it is the Kth distinct element or Kth element in sorted order depending on the variant, but for standard IBM assessments, it refers to the Kth element when the array is sorted (allowing duplicate values to count as separate elements). K is 1-indexed (e.g., K = 1 means the 1st smallest/largest element).

📥 Input Format

• The first line contains two space-separated integers: N (the size of the array) and K.
• The second line contains N space-separated integers, representing the elements of the unsorted array.

📤 Output Format

• Print two space-separated integers: the Kth smallest element followed by the Kth largest element.

📋 Constraints

• \(1 \le K \le N \le 10^5\)
• \(-10^9 \le A[i] \le 10^9\)
• Optimal Target: Time Complexity: \(O(N)\) average case using Quickselect, or \(O(N \log K)\) using Min/Max Heaps.

🎯 Sample Cases


Sample Input 1

text
6 2
7 10 4 3 20 15
Use code with caution.

Sample Output 1

text
4 15
Use code with caution.

Explanation 1

If we sort the array in ascending order: [3, 4, 7, 10, 15, 20]
• The 2nd smallest element (K=2) is 4.
• The 2nd largest element (K=2) from the end is 15.
"""

def sl(arr,k):


    arr.sort()

    N = len(arr)

    if k == N:
        return -1


    target = arr[k-1]

    




print(sl([7, 10, 4, 3, 20, 15], 2))