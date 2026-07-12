# Q1 Write a program the percentage of student based on mark of any 5 subject.

#take 5 subject
sub1=int(input('enter marks the subject 1 ' ))
sub2=int(input('enter marks the subject 2 ' ))
sub3=int(input('enter marks the subject 3 ' ))
sub4=int(input('enter marks the subject 4 ' ))
sub5=int(input('enter marks the subject 5 ' ))

# calculate the total marks
total_marks = sub1 + sub2 + sub3 + sub4 + sub5

#perform the percentage 
percentage= (total_marks/500)*100

#display result
#print(f'percentage of 5 subject marks {total_marks} is {precentage}')