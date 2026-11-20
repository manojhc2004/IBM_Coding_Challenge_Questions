"""Given a list of names determine the number of names in that list for which a given query string is a prefix The prefix must be at least 1 character less than the entire name string Example

example:
names = ['jackson', 'jacques','jack']
query = ['jack']

! prefix always start from the first character""" 

name = ['jackson', 'jacques','jack']
q = ['jack',"j","jac"]

def prefixstring(names,query):


    output = []
    hm = {}

    for i in range(len(names)):

        curr = names[i]
        for end in range(1, len(curr)):

            prefix = curr[:end]
            hm[prefix] = hm.get(prefix, 0)+1
        
    
    # edge return all the queries total prefix count

    for q in query:
        output.append(hm[q])
    
    return output


print(prefixstring(name,q))