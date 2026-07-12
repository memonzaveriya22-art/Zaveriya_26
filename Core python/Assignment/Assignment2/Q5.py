# Q5 write a program to calculate selling price of book based on cost price and discount.

cost_price=int(input('enter the book cost price '))
discount_percent=int(input('enter the book discount percent '))
#discount_amount=int(input('enter the book discount amount '))

selling_price= (cost_price)* (1-discount_percent/100)
#selling_price= cost_price - discount-amount

print(f'Total selling price of book is {selling_price} ')