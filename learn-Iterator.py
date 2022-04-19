fruit_list = ["apple", "banana", "cherry"]
data = iter(fruit_list)

print(next(data))
print(next(data))
print(next(data))


class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


obj = Numbers()
data_obj = iter(obj)

print(next(data_obj))
print(next(data_obj))
print(next(data_obj))


class Colors:
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.rgb):
            raise StopIteration

        # return the next color
        color = self.rgb[self.__index]
        self.__index += 1
        return color


obj1 = Colors()
data_obj1 = iter(obj1)

print(next(data_obj1))
print(next(data_obj1))
print(next(data_obj1))
