# A generator function
def simpleGenerator():
    yield 1
    yield 2
    yield 3


# x is a generator object
data = simpleGenerator()

# Iterating over the generator object using next
print(next(data))
print(next(data))
print(next(data))


# create simple generator for Fibonacci Numbers

def fib(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
fib_data = fib(5)

# Iterating over the generator object using next
print(next(fib_data))
print(next(fib_data))
print(next(fib_data))
print(next(fib_data))
print(next(fib_data))
