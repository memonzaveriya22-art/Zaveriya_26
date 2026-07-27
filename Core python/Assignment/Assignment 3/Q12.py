# Q12. Write a program to check if given 3 digit number is a palindrome or not.

num= int(input('Enter number: '))

temp = num
rev = 0
while(num > 0):
    d = num % 10
    num = num // 10
    rev = rev * 10 + d
    print(d)

if(temp == rev):
    print('it is pallindrom')
else:
    print('it is not palindrom')