def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


if __name__ == "__main__":
    a = 1
    b = 2

    result = add(a, b)

    print("{} + {} = {}".format(a, b, result))
