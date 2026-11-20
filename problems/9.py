"""20. Valid Parentheses (Easy)

premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

strr = "{[]}"

def validpara(s):


    hm = {")":"(", "}": "{", "]":"["}

    stack = []
    
    for i in s:
        if (i in hm) and (stack) and (hm[i] == stack[-1]):
            stack.pop()
        # edge case 1
        elif (i in hm) and (stack) and (hm[i]!= stack[-1]):
            return False
        else:
            stack.append(i)

    # edge case 2
    if stack:
        return False

    return True

print(validpara(strr))