# Q11. WAP to check if given number Strong Number.

number_str = input("Enter a number: ")
total_sum = 0

for character in number_str:
    digit = int(character) 
    
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
        
    total_sum = total_sum + fact

if total_sum == int(number_str):
    print("It is a Strong Number!")
else:
    print("It is NOT a Strong Number.")