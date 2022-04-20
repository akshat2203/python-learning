"""
# Basic structure for try except
try:
   # do something
   pass
except:
   # handle all exceptions
   pass
else:
    # run this code if no exception occurs
    pass
finally:
    # always run this code
    pass
"""

# Ex - 1
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except Exception as e:
    print(e)
    print("Not an even number!")
else:
    reciprocal = 1 / num
    print(reciprocal)

# Ex - 2
try:
    a = 10 / 0
except(ArithmeticError, IOError):
    print("Arithmetic Exception")
else:
    print("Successfully Done")

# Ex - 3
try:
    file = open("file2.txt", "r")
    try:
        file.write("Hello, I am good")
    finally:
        file.close()
        print("file closed")
except Exception as e:
    print(e)
    print("Error")


# Ex - 4
def get_data(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers")
        print(Argument)


# get_data("Asdf")
value = get_data("10")
print(value)

# Ex - 5
try:
    file = open("test_file", "w")
    file.write("This is my test file for exception handling!!")
except FileNotFoundError:
    print("Wrong file or file path")
finally:
    print("code run")
