"""Return the maximum-sum subarray"""


arr = [-2, 1, -3, 4, -1, 2]
def maxsubc(arr):

    currsum = arr[0]
    maxsum = arr[0]

    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(arr)):

        if arr[i] > currsum + arr[i]:
            currsum = arr[i]
            temp_start = i
        else:
            currsum += arr[i]

        if currsum > maxsum:
            maxsum = currsum
            start = temp_start
            end = i

    return arr[start:end+1], maxsum




print(maxsubc(arr))