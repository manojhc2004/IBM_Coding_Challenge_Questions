"""Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Example

There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type .

Function Description

Complete the migratoryBirds function in the editor below.

migratoryBirds has the following parameter(s):

int arr[n]: the types of birds sighted
Returns

int: the lowest type id of the most frequently sighted birds"""



def migrateBird(s):

    hash = {}
    maxx = float("-inf")
    value = float("inf")

    for i in s:

        if i in hash:

            hash[i] +=1
            if (hash[i] > maxx):
                maxx = hash[i]
                value = i 

            elif (hash[i] == maxx) and (i < value):
                value = i 
            
        else:
            hash[i]  = 1
    

    return value 

    

if (__name__ == "__main__"):

    birds = [1,2,1,3,5,5,6,7,1]

    call = migrateBird(birds)
    print(call)