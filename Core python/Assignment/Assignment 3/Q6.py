# Q6. 6. Write a program to calculate profit or loss.

cost_price = int(input("Enter the cost price (buying price): "))
selling_price = int(input("Enter the selling price: "))

# 2. Check for profit
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("You made a profit!")
    print("Profit amount:", profit)

# 3. Check for loss
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("You made a loss.")
    print("Loss amount:", loss)

# 4. If prices are exactly equal
else:
    print("No profit, no loss. You broke even!")