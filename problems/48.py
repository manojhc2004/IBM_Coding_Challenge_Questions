"""Problem 11 – Longest Substring Without Repeating Characters
IBM-style practice
Medium
Sliding Window + HashMap

Problem statement
You are given a string S. Your task is to find the length of the longest contiguous substring that contains no repeating characters.

Input format:
A single string S.

Sample Input 1
abcabcbb


Sample Output 1
3


Explanation: The longest substring without repeating characters is abc.

Sample Input 2
bbbbb


Sample Output 2
1"""


def longest(arr):


    maxx = 0
    left = 0
    hash = {}

    for right in range(len(arr)):

        hash[arr[right]] = hash.get(arr[right], 0)+1

        while hash and hash[arr[right]] > 1:
            hash[arr[left]]-=1
            left+=1
        
        if maxx < (right - left + 1):
            maxx = right - left +1
        

    return maxx
        

        
        
print(longest("pwwkew"))