def raise_exception():
    x = "hello"
    y = 5
    if not isinstance(y, str):
        raise TypeError("Only string values are allowed")
