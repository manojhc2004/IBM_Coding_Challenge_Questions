"""IBM ASE – DSA Practice Question
Easy | Arrays | Iteration
Problem: Transmission Packet Counter

A data transmission system receives a sequence of binary digits (0s and 1s).

The system can transmit only a continuous sequence of identical digits in a single packet. Whenever the digit changes from 0 to 1 or from 1 to 0, a new packet is required.

Given an array representing the transmission sequence, find the minimum number of packets required to transmit the entire sequence.

Input:
arr = [1,1,0,0,1,0,1,1,1,0,1]



Output:
7


Explanation:

The transmission is divided into these groups:
[11] [00] [1] [0] [111] [0] [1]"""



def requiredpackets(arr):

    packets = 1

    for i in range(1, len(arr)):

        
        if(arr[i] != arr[i-1]):
            packets+=1
        
    return packets





print(requiredpackets([1,1,0,0,1,0,1,1,1,0,1]))