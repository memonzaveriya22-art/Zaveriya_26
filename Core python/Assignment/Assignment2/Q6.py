# Q6 write a program to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

basic_salary = int(input('Enter the value of basic salary. '))

da=0.10*basic_salary
ta=0.12*basic_salary
har=0.15*basic_salary

total_salary= basic_salary + da + ta + har

print(f'The Total salary of Employee is {total_salary} ')