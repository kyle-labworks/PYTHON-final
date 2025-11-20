import math

# String functions
text = "   Hello World   "
print("Original:", text)
print("Length:", len(text))
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Stripped:", text.strip())
print("Replaced:", text.replace("World", "Python"))
print("Split:", text.split())

# Math functions
num = 16
print("\nSquare Root:", math.sqrt(num))
print("Power (2^5):", pow(2, 5))
print("Absolute:", abs(-20))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.9))
print("Factorial:", math.factorial(5))
print("Cos 60°:", math.cos(math.radians(60)))
print("PI value:", math.pi)
