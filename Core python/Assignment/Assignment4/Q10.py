# Q10. WAP to check if given number is Perfect Number.

num = int(input("Enter a number: "))
is_perfect = sum(i for i in range(1, (num // 2) + 1) if num % i == 0) == num
print(f"Perfect number status: {is_perfect}")
