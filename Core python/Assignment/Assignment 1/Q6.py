# Q6 write a program to input two angle from user and find the angle of the triangle.

# Take a input from user
Angle1 = int(input('Enter the first angle of triangle. '))
Angle2 = int(input('Enter the second angle of triangle. '))

# calculate the formula

triangle = 180 - Angle1 + Angle2

#Display the result
print(f'Third Angle of triangle is {triangle} ')

