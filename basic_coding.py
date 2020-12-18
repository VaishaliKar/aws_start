print("Hi all")
studentRollno=100
studentName=("Bob")
studentAge=(1)

#Can get input from 15 users
count=0
while count < 15:
    studentRollno=int(input("Enter your Roll number"))
    studentName=input("Enter your name")
    studentAge=input("Enter your age")
    marks=int(input("Enter your marks"))
    
    #display details
    print("Student Details")
    print("Roll Number: {0}, Name: {1}, Age: {2}, marks: {3} ".format(studentRollno,studentName,studentAge,marks))
    




count=0
