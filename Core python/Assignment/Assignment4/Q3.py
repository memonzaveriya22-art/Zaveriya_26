# Q3. WAP to print sum of series upto n.

n = int(input('Enter the value of n: '))

sum_series = 0


for i in range(1, n + 1):
    sum_series += i
print(f'The sum of the series up to {n} is {sum_series}')