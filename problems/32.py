"""1. Find the second largest element in an unsorted array without sorting."""


def secondlargest(arr):


    first = arr[0]
    second = arr[0]


    for i in range(1,len(arr)):

        if arr[i] > first:
            second = first
            first = arr[i]
        
        elif arr[i] < first and second < arr[i]:

            second = arr[i]
    

    return first,second



print(secondlargest([1,9,6,4,3,8]))