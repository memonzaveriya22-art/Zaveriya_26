# Q10 Write a program to reverse three-digit number.

num=int(input('Enter the number '))

a=num%10
b=num//10%10
c=num//100
res=a*100+b*10+c
print(f'Reversed number is {res} ')