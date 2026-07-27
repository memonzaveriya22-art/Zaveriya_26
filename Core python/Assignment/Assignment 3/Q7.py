# Q7. Write a program to check if user has entered correct userid and password.

USER_ID = "admin123"
PASSWORD = "SecretPassword"


user_id = input("Enter your User ID: ")
password = input("Enter your Password: ")

if user_id == USER_ID and password == PASSWORD:
    print("Login successful! Welcome to the system.")
else:
    print("Login failed! Incorrect User ID or Password.")