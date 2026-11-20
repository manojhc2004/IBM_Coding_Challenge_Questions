"""A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late ().

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled."""


def angryProfessor(k, a):
    # Write your code here
    
    early_students = 0
    for i in a:
        if (i < 1):
            early_students +=1
    
    if (early_students < k):
        return "YES"
    return "NO"