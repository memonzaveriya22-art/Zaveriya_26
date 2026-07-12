# Q7 Program to find the Roots of quadratic Equation.

#take input from user

a= int(input('Enter the A value '))
b= int(input('Enter the B value '))
c= int(input('Enter the C value '))

# calculating the formula
z=b**2-4*a*c

Quadratic_Equation1=-b+(z**0.5)/2*a
Quadratic_Equation2=-b-(z**0.5)/2*a


print(f'Root of Quadratic Equation is {Quadratic_Equation1} ')
print(f'Root of Quadratic Equation is {Quadratic_Equation2} ')