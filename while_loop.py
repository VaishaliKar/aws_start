counter = 0
while counter < 4:
 age=int (input("What is your age in years?")
 if age >= 18:
     print("You are an adult.")
 elif age >= 13 and age <= 18:
     print ("You are a Teenager!")
 else:
     print("You are a child.")
 counter = counter + 1
