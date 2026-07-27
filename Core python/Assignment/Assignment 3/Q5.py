# Q5 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle

a1=int(input('Enter the first side= '))
a2=int(input('Enter the second side= '))
a3=int(input('Enter the third side= '))

if a1 == a2 == a3:
    print('This is an Equilatera Triangle.')
elif a1 == a2 or a2 == a3 or a1 == a3:
    print('This is an Isosceles Triangle.')
else:
    print('This is a Scalene Triangle.')