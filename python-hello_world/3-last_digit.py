import random

number = random.randint(-10000, 10000)

# Calculate the last digit of the number
last_digit = abs(number) % 10
# Ensure the last digit has the correct sign for negative numbers
last_digit *= -1 if number < 0 else 1

# Print the result
print(f"Last digit of {number} is {last_digit}", end=' ')

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
