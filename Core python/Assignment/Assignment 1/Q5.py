# Q5 Write the program to enter P, T, R and calculate Compound Intrest.

#take input P, T, R
P= int(input('Enter the principle amount '))
R= int(input('Enter the rate of intrest '))
T= int(input('Enter the time in years '))
n= int(input('Enter the number of compound '))

# calculate the formula
compound_intrest = P*(1+R/n)**n*T

# Display result
print(f'compound intrest is {compound_intrest} ')