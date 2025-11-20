# 1. if
score = int(input("Enter your score: "))
if score >= 75:
    print("You passed!")

# 2. if-else
num = int(input("\nEnter a number: "))
if num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

# 3. if-elif-else
marks = int(input("\nEnter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# 4. Nested if
n = int(input("\nEnter a number to check positivity and divisibility: "))
if n != 0:
    if n > 0:
        print("Positive", end=" ")
    else:
        print("Negative", end=" ")

    if n % 2 == 0:
        print("and divisible by 2")
    else:
        print("and not divisible by 2")
else:
    print("The number is zero")
