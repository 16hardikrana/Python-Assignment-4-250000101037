import math

def circle_area(radius):
    return math.pi * radius ** 2

radius = float(input("Enter radius: "))
print("Area:", round(circle_area(radius), 4))
