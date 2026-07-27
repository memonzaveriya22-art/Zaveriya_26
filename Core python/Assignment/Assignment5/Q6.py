#Q6. Write a program to print first n prime numbers.

n = int(input('Enter the value of n: '))

count = 0
number = 2

print(f' The first {n} prime number are: ')

while count < n:
    prime = True 

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        print(number, end=" ")
        count = count+1
    number = number + 1