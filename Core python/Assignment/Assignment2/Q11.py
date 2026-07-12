#  Q11  Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount

amount=int(input('enter the amount' ))
print()

notes_500 = amount//500
amount = amount-(notes_500*500)
print('500 notes:' ,notes_500)

notes_100 = amount//100
amount = amount-(notes_100*100)
print('100 notes:' ,notes_100)


notes_50 = amount//50
amount = amount-(notes_50*50)
print('50 notes:' ,notes_50)


notes_10 = amount//10
amount = amount-(notes_10*10)
print('10 notes:' ,notes_10)

total = notes_500 + notes_100 + notes_50 + notes_10
print()
print('Minimum notes needed is:',total )