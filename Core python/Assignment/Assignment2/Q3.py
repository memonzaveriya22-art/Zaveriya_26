# Q3 convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

total_inches = (feet * 12) + inches

total_cm = total_inches * 2.54

meters = int(total_cm // 100)
centimeters = round(total_cm % 100, 2)


print(f"Result: {meters} meters and {centimeters} centimeters")