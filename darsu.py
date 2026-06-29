# BASIC PYTHON PRACTICE
# Topics:
# - Variables & Data Types
# - Operators
# - Type Conversion
# - User Input
# - Practice Questions


# ---------------
# Printing Output
# ----------------

print("Darshana")
print("My age is 19")

print("Darshana. My age is 19")
print(23)
print(32)
print(23 + 32)

# ------------------------
# Variables and Data Types
# -------------------------
name = "Darshana"
age = 23
price = 25.99

print(name)
print(age)
print(price)

print("My name is:", name)
print("My age is:", age)
print("My price is:", price)

# Copying variable value
age2 = age
print(age2)

# Checking data types
print(type(name))
print(type(age))
print(type(price))

# Different ways to create strings
name1 = "darsu"
name2 = 'darsu'
name3 = '''darsu'''

print(name1)
print(name2)
print(name3)

# Boolean and None data types
age3 = 23
old = False
a = None

print(type(old))
print(type(a))

# ---------------------
# Arithmetic Operations
# ----------------------

a = 3
b = 8

result = a + b
print("Addition:", result)

c = 3
d = 8

result = c - d
print("Subtraction:", result)

# ------------------------------------------
# Arithmetic Operators
# ------------------------------------------

e = 5
f = 10

print("Addition:", e + f)
print("Subtraction:", e - f)
print("Multiplication:", e * f)
print("Division:", e / f)
print("Modulus:", e % f)
print("Power:", e ** f)

# ------------------------------------------
# Relational Operators
# ------------------------------------------

g = 30
h = 10

print(g == h)
print(g != h)
print(g > h)
print(g >= h)
print(g < h)
print(g <= h)

# ------------------------------------------
# Assignment Operators
# ------------------------------------------

num = 10
num = num + 10
print("num:", num)

pye = 10
pye += 10
print("pye:", pye)

# ------------------------------------------
# Logical Operators
# ------------------------------------------

i = 50
j = 30

# NOT operator
print(not False)
print(not (i > j))

# AND operator
val1 = True
val2 = False

print("AND operator:", val1 and val2)

# OR operator
print("OR operator:", val1 or val2)
print("OR operator:", (i == j) or (i > j))

# ------------------------------------------
# Type Conversion
# ------------------------------------------

k = 2
l = 4.24

result = k + l
print("Type conversion:", result)

ab = int("5")
ba = 4.28

result = ab + ba
print(type(ab))
print("Type conversion:", result)

# ------------------------------------------
# User Input
# ------------------------------------------

input("Enter your name: ")

surname = input("Enter your surname: ")
print("Thank you", surname)

value = input("Enter some value: ")
print(type(value), value)

value1 = int(input("Enter a number: "))
print(type(value1), value1)

# ------------------------------------------
# User Information Program
# ------------------------------------------

name = input("Enter name: ")
age = input("Enter age: ")
marks = input("Enter marks: ")

print("Welcome", name)
print("Age =", age)
print("Marks =", marks)

# ==========================================
# Practice Questions
# ==========================================

# Question 1: Sum of two numbers

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("Sum =", first + second)

# Question 2: Area of a square

side = float(input("Enter square side: "))
print("Area =", side ** 2)

# Question 3: Average of two numbers

y = float(input("Enter first number: "))
z = float(input("Enter second number: "))

print("Average =", (y + z) / 2)

# Question 4: Check if first number is greater than
# or equal to second number

w = float(input("Enter first number: "))
x = float(input("Enter second number: "))

print(w >= x)