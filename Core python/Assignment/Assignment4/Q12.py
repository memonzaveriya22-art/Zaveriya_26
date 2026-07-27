# Q12. 12. Write a program to check if given number is Armstrong number or not.
#Hint: 1531*1*1+5*5*5+3*3*3, 1634 = 1*1*1*1+6*6*6*6+3*3*3*3+4*4*4*4)

num = int(input("Enter a number: "))

num_str = str(num)
power = len(num_str)

temp = num
total_sum = 0


while temp > 0:
    digit = temp % 10
    total_sum += digit ** power
    temp = temp // 10

if num == total_sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong.")