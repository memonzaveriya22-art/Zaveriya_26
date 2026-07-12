# Q1 convert the time entred in hh,min and sec into seconds.

# Take input from user

hours=int(input('Enter the value of hour '))
minutes=int(input('Enter the value of minutes '))
second=int(input('Enter the value of seconds '))

total_second= (hours*3600)+(minutes*60)+second

print(f'total second is {total_second} ')