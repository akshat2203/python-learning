# Python code to illustrate split() function
with open("test_file", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)


# Python code to write mode
file = open('new_file.txt', 'w')
file.write("This is for test")
file.close()

# Python code to illustrate append() mode
file = open('new_file.txt', 'a')
file.write("This will add this line")
file.close()


with open("test.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
    f.close()


with open("test.txt", 'r', encoding='utf-8') as f:
    print(f.read(4))  # read the next 4 data
    print(f.read())  # read in the rest till end of file

    print(f.tell())  # get the current file position
    print(f.seek(0))  # bring file cursor to initial position

    print(f.readline())
