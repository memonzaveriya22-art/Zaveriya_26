# Q4 write a program to enter P, T, R and calculate simple intrest.

#take input P, T, R
P= int(input('Enter the principle amount '))
R= int(input('Enter the rate of intrest '))
T= int(input('Enter the time in years '))

#calculate the formula
simple_intrest= P*R*T/100

#display result
print(f'simple intrest is {simple_intrest}')
