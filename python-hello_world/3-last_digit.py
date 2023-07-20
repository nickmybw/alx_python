import random


def get_last_digit(number):
    return abs(number) % 10


# Positive case
number = random.randint(1, 10000)
last_digit = get_last_digit(number)
print(f"Last digit of {number} is {last_digit}", end=' ')
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

# Negative case
number = random.randint(-10000, -1)
last_digit = get_last_digit(number)
print(f"Last digit of {number} is {last_digit}", end=' ')
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

# Zero case
number = 0
last_digit = get_last_digit(number)
print(f"Last digit of {number} is {last_digit}", end=' ')
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

# Wrong type case
try:
    number = "invalid"
    last_digit = get_last_digit(number)
    print(f"Last digit of {number} is {last_digit}", end=' ')
    if last_digit > 5:
        print("and is greater than 5")
    elif last_digit == 0:
        print("and is 0")
    else:
        print("and is less than 6 and not 0")
except TypeError as e:
    print("TypeError")
