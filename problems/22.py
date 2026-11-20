""". Write a program to find HCF of two numbers by without using recursion.
Input format: The first line contains any 2 positive numbers separated by space.

Output format:

Print the HCF of given two numbers.
Sample Input:

70 15
Sample Output:

5"""


def hcf(n1,n2):


    if (n1 == 0) or (n2==0):
        return 0
    
    while n2 !=0:

        n1,n2 = n2, n1 % n2


    print(n1)


print(hcf(20,5))