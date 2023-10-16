# Variable Names - A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)
# 5. A variable name cannot be any of the Python keywords.

# Creating Variables - Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

# Casting - If you want to specify the data type of a variable, this can be done with casting.

x = str(3)  # x will be '3'
print(type(x))
y = int(3)  # y will be 3
print(type(y))
z = float(3)  # z will be 3.0
print(type(z))

# Case-Sensitive - Variable names are case-sensitive.
a = 4
print(a)
A = "Sally"
print(A)

# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection - If you have a collection of values in a list, tuple etc. Python allows you to extract the
# values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables - Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# --------------------------------------------

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# --------------------------------------------

# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)