"""
Consider a string S that is a series of characters each followed by ites frequency as an integer the string is not compressed correctly so there may be multiple occurences of the same character A properly compressed string will consist of one instance of each character in alphabetical order followed by the total count of that character within the string.

"""


def compress(s):


    res = []
    freq  = {}

    i = 0

    while i < len(s):

        curr = s[i]

        i+=1
        count = ""
        while (i < len(s)) and (s[i].isdigit()):

            count+= s[i]
            i+=1
        

        toint = int(count)

        freq[curr] = freq.get(curr,0)+toint


    for key in sorted(freq):

        res.extend([key] * freq[key])

    
    return "".join(res)

    
    
        

print(compress("a7b4c7a2g5a2b2c1"))