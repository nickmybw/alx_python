def pow(a, b):
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result


#!/usr/bin/env python3
pow = __import__('1-power').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
#