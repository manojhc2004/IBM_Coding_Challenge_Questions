"""A scheduling system stores multiple time intervals representing bookings. Overlapping bookings
must be merged to produce an optimized schedule.
Input Format
First line: integer n
Next n lines: two integers start end
Output Format
Print merged intervals in sorted order.
Constraints

1 ≤ n ≤ 10^5
0 ≤ start ≤ end ≤ 10^9
    Sample Input

    4
    1 3
    2 6
    8 10
    15 18

Sample Output
    1 6
    8 10
    15 18"""


def mergeinterval(n, arr):



    # Sort the array based on start times
    arr.sort()

    res = [arr[0]]

    for i in range(1, len(arr)):
        curr = arr[i]

        # Fix 1: Use >= to capture intervals that touch at the edges


        if (res[-1][1]) >= (curr[0]):

            res[-1] = [res[-1][0], max(res[-1][1], curr[1])]


        else:
            res.append(curr)
    
    return res




print(mergeinterval(4, [[1, 3], [2, 6], [ 8, 10], [15, 18]] ))