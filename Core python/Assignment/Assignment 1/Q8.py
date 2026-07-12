# Q8  Write a program to convert days into years, weeks and days.

g_days=int(input('enter your days '))
years=g_days//365
r_days=g_days%365
week=r_days//7
days=r_days%7

print(f'Year: {years}, Week:{week}, Days:{days}')
