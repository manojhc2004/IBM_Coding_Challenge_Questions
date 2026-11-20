"""
Problem Statement: Extract and Process System Log Quantities


Description

An automated asset tracking system logs transactional updates as a single alphanumeric string. Due to system glitches, text and numeric values have been merged without standard delimiters.
Your task is to write an algorithm that parses this log string, extracts all distinct integer quantities, and returns them in the order they appear. If a number is repeated in the text, it should only be included once in the final output (maintaining its first appearance).

Input Format

• A single string log_string containing lowercase/uppercase English letters, spaces, and digits.

Constraints

• \(1 \le \text{length of } log\_string \le 10^5\)
• The numbers extracted fit within a standard 32-bit signed integer.

Output Format

• Return an array (or list) of integers representing the unique numbers extracted from the string in their chronological order of appearance. If no numbers are found, return an empty array.


• Input: log_string = "system encountered 12 errors while processing 404 requests and 12 warnings"
• Output: [12, 404]

"""


def extractnum(s):


    hm = {}

    N = len(s)

    i = 0
    while i < N:

        curr = ""

        while (i < N) and (s[i].isdigit()):

            curr+= s[i]
            i+=1

        if curr:
            toint = int(curr)
            hm[toint] = hm.get(toint,0)+1

        i+=1


    output = list(hm.keys())

    return output
    




    

    

print(extractnum("id value maxes out at 2147483647 units"))