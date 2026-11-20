"""An equilibrium index of a 0-indexed array is an index i such that the sum of elements at lower indices is equal to the sum of elements at higher indices.
More formally, i is an equilibrium index if:

\(\sum _{j=0}^{i-1}A[j]=\sum _{k=i+1}^{n-1}A[k]\)
• If i = 0, the sum of lower elements is assumed to be 0.
• If i = n - 1, the sum of higher elements is assumed to be 0.

Write a program that takes an array of integers and returns the first (lowest) equilibrium index. If no equilibrium index exists, return -1.

📥 Input Format

• The first line contains an integer N, denoting the size of the array.
• The second line contains N space-separated integers, representing the elements of the array.

📤 Output Format

• Print a single integer representing the lowest equilibrium index, or -1 if none exists.

📋 Constraints

• \(1 \le N \le 10^5\)
• \(-10^5 \le A[i] \le 10^5\)

🎯 Sample Cases


Sample Input 1

text
7
-7 1 5 2 -4 3 0
Use code with caution.

Sample Output 1

text
3"""



def equilibrium(n, arr):

    
    i = 0
    j = len(arr)-1

    leftsum = 0
    rightsum = 0

    while i < j:

        leftsum+= arr[i]
        rightsum+= arr[j]

        if (leftsum == rightsum):
            return i + 1
        j-=1
        i+=1
    
    return -1
        


print(equilibrium(5, [1, -1, 0, 5, -5]))