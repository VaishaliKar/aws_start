def new_user()
    confirm = "N"
    while confirm!= "Y":
        username = str(input("Please enter the name of the user to add:"))
        print("User the username" + username + "?(Y/N")
        confirm = str(input("")).upper()
        os.system("sudo adduser" + username)

def remove_user()
    confirm = "N"
    while confirm !="Y"
      username = str(input("Please enter the name of the user to remove:"))
        print("Remove the user" + username + "?(Y/N")
        confirm = str(input("")).upper()
        os.system("sudo del-userdel-r" + username)

