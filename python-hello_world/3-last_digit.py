import random


def last_digit(number):
  """
  Returns the last digit of a number.

  Args:
    number: The number to get the last digit of.

  Returns:
    The last digit of the number.
  """

  last_digit = number % 10
  return last_digit


def main():
  """
  Prints the last digit of a number and its corresponding condition.
  """

  number = random.randint(-10000, 10000)
  last_digit = last_digit(number)

  if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
  elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
  else:
    print(
        f"Last digit of {number} is {last_digit} and is less than 6 and not 0")


if __name__ == "__main__":
  main()
