if __name__ == "__main__":
    try:
        import variable_load_2
        print(variable_load_2.a)
    except AttributeError:
        print("a missing")
