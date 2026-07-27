# Q13. 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

units = int(input("Enter total units consumed: "))


if units <= 50:
    base_cost = units * 0.50
    
elif units <= 150:
    
    base_cost = (50 * 0.50) + ((units - 50) * 0.75)
    
elif units <= 250:
    
    base_cost = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
    
else:

    base_cost = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

surcharge = base_cost * 0.20

total_bill = base_cost + surcharge

print("Base Cost: Rs.", base_cost)
print("Surcharge: Rs.", surcharge)
print("Total Bill: Rs.", total_bill)