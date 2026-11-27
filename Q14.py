def square_and_cube(number):
    return number ** 2, number ** 3

number = int(input("Enter a number: "))
square, cube = square_and_cube(number)
print("Square:", square)
print("Cube:", cube)
