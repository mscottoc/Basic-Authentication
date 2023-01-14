# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
import json

with open('Lab02.json') as json_file:
    data = json.load(json_file)


CurrUser = input('Username: ')

AllUsers = data['username']
AllPasswords = data['password']
UserPresent = False
i = 0
while(i < len(AllUsers)):
    if (CurrUser == AllUsers[i]):
        UserPresent = True
        break
    else:
        i += 1


CurrPassword = input("Password: ")
PassMatch = False
if (CurrPassword == AllPasswords[i]):
    PassMatch = True

if (UserPresent == True or PassMatch == True):
    print("You are authenticated!")
else:
    print('You do not have access to this system')
