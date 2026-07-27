# Q9 Input 5 subject marks from user and display grade(eg. First class, Second class..

s1=int(input('Enter the subject1 Marks: '))
s2=int(input('Enter the subject1 Marks: '))
s3=int(input('Enter the subject1 Marks: '))
s4=int(input('Enter the subject1 Marks: '))
s5=int(input('Enter the subject1 Marks: '))

total_marks=s1+s2+s3+s4+s5
avarage_marks=total_marks/50

if avarage_marks >=60:
    print('Result: pass - First class')
