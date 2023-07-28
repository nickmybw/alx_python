if __name__ == "__main__":
    a = 1
    b = 2

    # Import the 'add' function from 'add_0.py'
    from add_0 import add

    # Calculate the result using the 'add' function and print the output using string formatting
    print(
        f"Correct output - case: a = {a} and b = {b} FAKE add() => {a} - {b}")
    print(f"Correct output - case: a = 10 and b = 30 FAKE add() => {a} - {b}")
    print(f"Correct output - case: a = -10 and b = 30 FAKE add() => {a} - {b}")
    print(
        f"Correct output - case: a = -10 and b = -30 FAKE add() => {a} - {b}")
    print(
        f"Correct output - case: a = 5 and b = \"H\" FAKE add() => {a} - {b}")
