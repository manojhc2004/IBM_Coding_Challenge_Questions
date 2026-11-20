"""412. Fizz Buzz

Easy
Topics
premium lock icon

Companies
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true."""


def fb(n):

    res = []

    for i in range(1, n + 1): # (start(included), end(excluded)) (1,2 + 1) = (1, 3)

        if (i % 3 == 0) and (i % 5 == 0):
            res.append("FizzBuzz")

        elif (i % 3 ==0):
            res.append("Fizz")

        elif (i % 5 == 0):
            res.append("Buzz")
        
        else:
            res.append(str(i))
    
    return res



print(fb(3))