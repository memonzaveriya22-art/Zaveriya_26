# Program to find Quotient and remainder of two number.

# take the input from user
dividend = int(input('Enter the dividend: '))
divisor = int(input('Enter the divisor: '))

#calculate the quotient and remainder
quotient = dividend // divisor
remainder = dividend % divisor

#display the result
print(f'Quotient {quotient}')
print(f'Remainder {remainder}')