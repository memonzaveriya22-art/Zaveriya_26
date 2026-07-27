# Q4 Write a program to input angles of a triangle and check whether triangle is valid or not.

a1=int(input('Enter the angle1: '))
a2=int(input('Enter the angle2: '))
a3=int(input('Enter the angle2: '))

if(a1+a2+a3==180):
    print('it is triangle valid')
else:
    print('it is not valid triangle')