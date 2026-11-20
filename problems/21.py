"""
A student copeing the words from another student making copeing of first line and second line then writing third line, then copeing second line and third line then writting 5 line same repeat
"""


def nsum(values, n):

    if (len(values) < 2) or (values[0] > values[1]) or (values[0] <=0) or (values[1] <=0) or (n <=2):
        return "INVALID"

    
    third = values[0] + values[1]
    fourth = values[1] + third

    if (n == 3):return third
    if (n == 4):return fourth

    res = 0
    i = 5
    while i < n+1:

        res = third + fourth
        print(res)
        third = fourth
        fourth = res 
        i+=1

    
    return res



print(nsum([1,2],8)) # 1,2,3,5,8,13 