# 1. Name:
#      M. Scott O'Connor
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program is a basic unsecure username and password system. 
#      It was created to practice my ability to read from a json file 
#      and convert the contents into whatever variable type is needed.
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part was making sure that the password 
#      matched the user name. In the end I decided to keep track
#      of which username was used by iterating through the list
#      and matching its place in the list with the same place in
#      the passwords list. It was also hard to figure out the syntax 
#      for this project as it seems that there are multiple valid
#      ways of importing a file, but only one best way.
# 5. How long did it take for you to complete the assignment?
#      1hr

import json

with open('Lab02.json') as json_file:
    data = json.load(json_file)

# retrieve username and password from the user
CurrUser = input('Username: ')
AllUsers = data['username']
AllPasswords = data['password']
# checks if user name is valid
UserPresent = False
i = 0
while(i < len(AllUsers)):
    if (CurrUser == AllUsers[i]):
        UserPresent = True
        break
    else:
        i += 1
# checks if password is valid only if the username matches
CurrPassword = input("Password: ")
PassMatch = False
if (UserPresent != False):
    if (CurrPassword == AllPasswords[i]):
        PassMatch = True
# only allows user if both username and password are valid
if (UserPresent == True and PassMatch == True):
    print("You are authenticated!")
else:
    print("You do not have access to this system")
