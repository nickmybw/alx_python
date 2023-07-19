import random
number = random.randint(-10, 10)

print(number, end=' ')

# YOUR CODE HERE
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")



