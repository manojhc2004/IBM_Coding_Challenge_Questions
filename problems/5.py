

student_skills = [0,1,3,5,8,9,15,16,18,20] # [8,9,12,13,14]


def decathlon(skills):

    skills = sorted(skills)

    output = 0
    curr = 0

    for i in range(len(skills)-1):

        if (skills[i+1] - skills[i] == 1):
            curr = 1
        else:
            if curr == 1:
                output+=1

            curr = 0
    
    if curr == 1:
        output+=1
    
    return output


print(decathlon(student_skills))