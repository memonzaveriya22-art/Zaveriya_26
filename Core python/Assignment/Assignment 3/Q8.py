# Q8 Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random
userid=input('enter the userid=')
password=input('enter the password=')
if userid=="admin" and password=="zaveriya26":
    captch=random.randint(1000,9999)
    print(type(captch))
    print(f'your captch= {captch}')
    chuser=input('enter the captch=>')
    if chuser==str(captch):
        print('user login succesfully..')
    else:
        print('invalid captch...')
else:
    print('user is invalid....')


