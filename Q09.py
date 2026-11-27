import math
angle = float(input("Enter angle in degrees: "))
radians = math.radians(angle)
print("Sine:", round(math.sin(radians), 4))
print("Cosine:", round(math.cos(radians), 4))
print("Tangent:", round(math.tan(radians), 4))
