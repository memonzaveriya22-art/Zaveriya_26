# Q5. WAP to print Fibonacci series upto n.

n = int(input('How many fibonacci number you want: '))
a = 1
b= 2

for i in range(n):
    c = a + b 
    print(c)

    a = b
    b = c