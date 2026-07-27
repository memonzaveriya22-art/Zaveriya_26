# Q4. WAP to print Armstrong number within a given range

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

print("Armstrong numbers are:")

for num in range(lower, upper + 1):
    
    if num < 10:
        if num > 0:
            print(num)
        continue
        

    num_str = str(num)
    num_of_digits = len(num_str)
    
    
    total_sum = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10          
        total_sum += digit ** num_of_digits  
        temp = temp // 10          
        
    if num == total_sum:
        print(num)