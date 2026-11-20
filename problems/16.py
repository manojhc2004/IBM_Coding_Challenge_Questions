"""Detect Suspicious Users

Problem Statement
A large authentication platform logs login attempts. Security analysts must identify accounts
repeatedly attempting logins, which may indicate brute-force attacks. A user is considered
suspicious if their user ID appears at least m times in the log dataset.
Input Format
First line: integer n (number of login attempts)
Second line: n space-separated integers representing user IDs
Third line: integer m (threshold)
Output Format
Print all user IDs that appear at least m times in ascending order.
Constraints
1 ≤ n ≤ 10^5
0 ≤ userId ≤ 10^9
1 ≤ m ≤ n
Sample Input
4
7 2 0 7
2

Sample Output
7
"""


def detect(n,userid,m):

    hashmap = {}
    count = 0

    for i in userid:
        hashmap[i] = hashmap.get(i, 0)+1
    

    for key, val in hashmap.items():

        if val >= m:
            count+=1
        

    return count



if (__name__ == "__main__"):


    n_ = 5
    users = [1,2,3,4,1]
    m_ = 1

    call = detect(n_,users,m_)
    print(call)