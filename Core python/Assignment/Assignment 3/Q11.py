# Q11. 11. Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition:
# a. Children below 12 30% discount
#b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age1=int(input('enter the age of First person='))
tkprice1=float(input('Enter the ticket price of the first person= '))
totalprice=0
if age1<12:
    totalprice=totalprice+(tkprice1*0.30)
elif age1>59:
    totalprice=totalprice+(tkprice1*0.50)
else:
    totalprice=totalprice+tkprice1
#first person ends here

age2=int(input('enter the age of second person='))
tkprice2=float(input('Enter the ticket price of the second person= '))
if age2<12:
    totalprice=totalprice+(tkprice2*0.30)
elif age2>59:
    totalprice=totalprice+(tkprice2*0.50)
else:
    totalprice=totalprice+tkprice2
#second person ends here

age3=int(input('enter the age of third person='))
tkprice3=float(input('Enter the ticket price of the third person= '))
if age3<12:
    totalprice=totalprice+(tkprice3*0.30)
elif age3>59:
    totalprice=totalprice+(tkprice3*0.50)
else:
    totalprice=totalprice+tkprice3
#third person ends here

age4=int(input('enter the age of fourth person='))
tkprice4=float(input('Enter the ticket price of the fourth person= '))
if age4<12:
    totalprice=totalprice+(tkprice4*0.30)
elif age4>59:
    totalprice=totalprice+(tkprice4*0.50)
else:
    totalprice=totalprice+tkprice4
# fourth person end here

age5=int(input('enter the age of fifth person='))
tkprice5=float(input('Enter the ticket price of the fifth person= '))
if age5<12:
    totalprice=totalprice+(tkprice5*0.30)
elif age5>59:
    totalprice=totalprice+(tkprice5*0.50)
else:
    totalprice=totalprice+tkprice5
#fifth person end here

print(f'Total prices to pay for the trip of five person is {totalprice}: ')