# Week 6 - Activity 1: List and dictionary data stucrture
# W6-A1 – Part 1:

# Develop an object-oriented project that creates:
# a dictionary to store five students, using student ID as the key and student name as the value, and
# a second dictionary using student ID as the key and MSE800 score as the value.
# W6-A1 – Part 2:

# Combine the two dictionaries from Part 1 and generate a new dictionary that includes only students who passed (score ≥ 50%).


class StudentRecord:
    def __init__(self):
        #dictionary to store 5 students - part 1
        self.student={
            '101':'Ram',
            '102':'Shyam',
            '103':'Hari',
            '104':'Sita',
            '105':'Harry'
        }
        
        
        # dictionary to store student id as key and MSE 800 score as value
        self.score={
            '101':90,
            '102':34,
            '103':89,
            '104':92,
            '105':50
        }
        
    #Part 2: Return only names of students who passed
    def passed_students(self):
        passed = []  #list
        for sid, marks in self.score.items():
            if marks >= 50:
                passed.append(self.student[sid])
        return passed 

#Main Program 
record = StudentRecord()

print("Student Dictionary:")
print(record.student)

print("\nPassed Students :")
print(record.passed_students())     

    
    

