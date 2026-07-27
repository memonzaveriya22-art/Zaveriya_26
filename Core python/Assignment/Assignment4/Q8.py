# Q8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

for num in range(lower_bound, upper_bound + 1):
    
    if num % 7 == 0 and num % 5 == 0:
        print(f"{num} is divisible by 7 and 5")