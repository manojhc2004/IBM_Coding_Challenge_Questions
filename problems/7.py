"""
String Decompression (Expansion)

This is the exact problem template used when IBM tests basic looping and string formatting.

Problem Statement

You are given a compressed string S where each character is immediately followed by an integer representing its frequency. Write a program to expand this string back to its original uncompressed form.

Input Format

A single line containing the compressed string S.

Output Format

A single line containing the expanded string.

Constraints

• 1 ≤ length of S ≤ 10⁴
• The string contains alternating lowercase English alphabets (a-z) and single-digit integers (0-9).

Sample Test Cases

• Sample Input 1: a3b5c2a2
• Sample Output 1: aaabbbbbccaa
• Sample Input 2: p1q4r0s2
• Sample Output 2: pqqqqss (Note: r0 means 'r' does not appear)"""


def uncompressed(s):

    hm = {}

    res = []

    for i in range(len(s)-1):

        if (s[i+1].isalpha() == False):
            res.extend([s[i]] * int(s[i+1]))
    

    
    return "".join(res)

    # preventing the edge case when they provide input : a12b13 then?? your code will only take a for 1 and b for 3 what about 12,13 so 
    # edge case
    """
    i = 0
    res = []
    while i < len(s):

        char = s[i]

        digit = ""
        while i < len(s) and s[i].isdigit():
            digit+= s[i]
            i+=1
        
        res.extend([char] * int(digit))
    
    
    return "".join(res)       

    """



print(uncompressed("a3b5c2a2"))