counter = 0
while counter < 3:
   myBunch=int(input("how many bananas do you have?"))
   if myBunch >= 5:
      print("Your bunch is large")
   elif myBunch >= 1 and myBunch <= 4:
      print("Your bunch is small")
   else:
      print("You have no bananas!")
   counter = counter + 1
