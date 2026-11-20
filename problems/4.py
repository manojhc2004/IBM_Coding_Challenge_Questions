"""IBM Internship HackerRank OA for 26 NG
Question 1: Frequent IP Addresses in a Time Window
Problem Statement

Given arrays of IP addresses and their respective timestamps, find all IP addresses that appear more than k times within any t-second window. If no such IP addresses exist, return an empty array.

Input

ip: an array of integers representing IP addresses.

timestamp: an array of integers representing the timestamps for each IP.

k: an integer threshold for the number of occurrences.

t: an integer representing the time window in seconds.

Output

An array of integers representing the IP addresses that appear more than k times within any t-second window. Return an empty array if none exist."""


def ipaddress(n,ip,timestamp,k,t): # parameters


    res = []
    hm = {}

    for i in ip:
        hm[i] = hm.get(i,0)+1
        if (hm[i] > k):
            res.append(i)
            

    if not res:
        return -1
    return res


print(ipaddress(3,[1, 2, 1], [6, 10, 15],1,10))



"""def ipaddress(n, ip, timestamp, k, t):
    from collections import defaultdict
    
    # Step 1: Group timestamps by IP address
    ip_times = defaultdict(list)
    for i in range(n):
        ip_times[ip[i]].append(timestamp[i])
        
    frequent_ips = []
    
    # Step 2: Use a sliding window for each IP's timestamps
    for current_ip, times in ip_times.items():
        # Ensure timestamps are sorted chronologically for the sliding window
        times.sort() 
        
        left = 0
        for right in range(len(times)):
            # Shrink the window from the left if the time gap exceeds t seconds
            while times[right] - times[left] > t:
                left += 1
            
            # The number of occurrences in the current window is (right - left + 1)
            if (right - left + 1) > k:
                frequent_ips.append(current_ip)
                break # Move to the next IP immediately once verified
                
    return frequent_ips

# Test Case from your example
# Explanation: IP 1 appears at 6s and 15s. Window size is 15-6 = 9s (which is <= 10s). 
# Total count for IP 1 in this window is 2, which is > k (1).
print(ipaddress(3, [1, 2, 1], [6, 10, 15], 1, 10))  # Output: [1]
"""