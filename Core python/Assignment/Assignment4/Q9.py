# Q9. WAP to print all numbers in a range divisible by a given number.

lower_limit = int(input("Enter the lower limit of the range: "))
upper_limit = int(input("Enter the upper limit of the range: "))
divisor = int(input("Enter the number to check divisibility by: "))

print(f"\nNumbers between {lower_limit} and {upper_limit} divisible by {divisor}:")

for number in range(lower_limit, upper_limit + 1):
    
    if number % divisor == 0:
        print(number)