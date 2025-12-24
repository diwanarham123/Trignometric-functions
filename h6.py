import math

degrees_str = input("Enter the angle in degrees: ")
try:
    degrees = float(degrees_str)
    radians = math.radians(degrees)

    print(f"Sine of {degrees} degrees: {math.sin(radians)}")
    print(f"Cosine of {degrees} degrees: {math.cos(radians)}")
    print(f"Tangent of {degrees} degrees: {math.tan(radians)}")
except ValueError:
    print("Invalid input. Please enter a valid number.")