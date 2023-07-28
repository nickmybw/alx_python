if __name__ == "__main__":
    try:
        # Import the variable 'a' from variable_load_2.py
        from variable_load_2 import a

        # Print the value of the variable 'a'
        print("Correct output - case: a =", a)
    except ImportError:
        print("Correct output - case: a missing")
