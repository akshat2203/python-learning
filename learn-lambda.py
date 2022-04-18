# create function to find double value
def double(x):
    return x * 2


print(double(5))  # output for above function

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

# Program to double each item in a list using map()
my_list1 = [1, 5, 4, 6, 8, 11, 3, 12]
new_list1 = list(map(lambda x: x * 2, my_list1))
print(new_list1)

# program for string lower cate to upper case using lambda
name = ['dog', 'cat', 'parrot', 'rabbit']
uppered_names = list(map(lambda animal: str.upper(animal), name))
print(uppered_names)

# Sort each sublist
List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
sort_list = lambda x: (sorted(i) for i in x)

# Get the second largest element
second_largest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = second_largest(List, sort_list)
print(res)
