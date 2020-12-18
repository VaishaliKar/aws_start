
def salute():
    print("Hello")
salute()

def greetall(): #defining function without argument
    return "Hello All!!!! "
result=greetall()
print(result)

def sayhi(name):
    print("hi " + name) #can use return instead of print
sayhi("Bunny")

def salute(studentName, Age):
    print("I am " + Age + "," +  studentName )
studentName = input("Enter your name")
Age = input("Enter your agein years")
salute(studentName, Age)

def greetlist():
    myList=["Hi", "Hello", 100, 25, "Bye"]
    return myList
print(greetlist())

#take an argument return he is a genius
def printgenius(name):
    return name + " is a genius."
print(printgenius("Vaishali"))

# to save input
studentName=input("Enter your name")
data=printgenius(studentName)
print(data)

#return use- if our code is used in website, but this print command is for the console or command line.
#assume if user is in browser so certain scenarios when other person is using console like you are
#you may have created a library for your project,reusability becomes easier with return when writing libraries return is handy

def greetlist():
    myList=["Hi", "Hello", 100, 25, "Bye"]
    return myList
for item in greetlist():
    print(item)

   
                    
