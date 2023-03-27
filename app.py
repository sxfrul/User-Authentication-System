database = {}
loginCondition = False

datafile = open("database.txt", "r")
for line in datafile:
    (key, val) = line.split()
    database[str(key)] = val
datafile.close()

# defining Login/Registry 
def registerPage():
    datafile = open("file.txt", "a+")
    userNewUsername = input("Please enter a new username: ")
    while userNewUsername in database:
        print("Name is already in the database")
        userNewUsername = input("Please try again: ")
    datafile.write("\n" + userNewUsername)

    userNewPassword = input("Please enter your new password: ")
    datafile.write(" "+ userNewPassword)
    print("\nRegistration process was succesful! You may now login.")
    datafile.close()

def loginPage():
    global loginCondition, userUsername
    userUsername = input("\nWhat is your username: ")
    while userUsername not in database:
        userUsername = input("Error, try again:")
    userPassword = input("Please enter your password: ")
    while userPassword != database.get(userUsername):
        userPassword = input("Error, please enter your password again (type ): ")
    loginCondition = True
    
# MAIN
while loginCondition == False:
    menuChoice= input("MENU:\n[1]Register\n[2]Login\n\nType here: ")
    if menuChoice == "2":
        loginPage()

    elif menuChoice == "1":
        registerPage()

print("Welcome back user#" + userUsername)



