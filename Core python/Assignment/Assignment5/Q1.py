# Q1. 1. Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.

CORRECT_USERID = "admin"
CORRECT_PASSWORD = "password123"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")
    if userid == CORRECT_USERID and password == CORRECT_PASSWORD:
        print("Login successful! Welcome.")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Incorrect credentials. You have {remaining} attempt(s) left.\n")
        else:
            print("Incorrect credentials.")