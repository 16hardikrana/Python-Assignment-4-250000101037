def greatest_number(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

print("Greatest:", greatest_number(11, 29, 17))
