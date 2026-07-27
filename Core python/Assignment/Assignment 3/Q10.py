Gender = input('Enter Gender(m/f): ')
age = int(input('Enter age: '))

if(Gender == 'f'):
    if(age >=18):
        print('Girl is Eligble for Marriage. ')
    else:
        print('Pehle Padhai kar lo. ')
else:
    if(age >= 21):
        print('Boys is Eligble for Marriage. ')
    else:
        print('Pehle kama kar lo.')
