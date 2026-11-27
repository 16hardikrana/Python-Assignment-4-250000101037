def greatest_of_three(a, b, c):
    greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c
    return greatest

print("Greatest:", greatest_of_three(15, 42, 27))
