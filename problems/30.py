"""
Question 1: String Compression / Frequency Tracker (Easy-Medium)

Problem Statement: You are given a compressed string consisting of letters followed by their counts, but the characters can repeat in different places (e.g., "a3b5c2a2"). Write a function to return the "properly compressed" version of the string where all identical characters are grouped together, and the output is sorted alphabetically.
• Example Input: "a3b5c2a2"
• Example Output: "a5b5c2" (Explanation: 'a' appears 3 times and then 2 times, totaling 5)"""


strr = "b2a3b5c2a2"
def compress(s):
 
    hash = {}
    
    i = 0
    while (i < len(s)):

        key = s[i]
        i+=1

        curr = ""
        while (i < len(s)) and (s[i].isdigit()):

            curr+= s[i]
            i+=1
        
        if key in hash:
            hash[key]+= int(curr)
        
        else:
            if (curr):
                hash[key] = int(curr)

    output = ""

    for key,val in sorted(hash.items()):

        output+=key + str(val)


    return output   

    
    

    
             


print(compress(strr))


