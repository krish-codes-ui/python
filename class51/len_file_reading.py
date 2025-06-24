try:
    file_name = open("poem.txt",'r')
    file = file_name.read()
    file_1 = file.split()
    print(len(file_1))
except FileNotFoundError:
    print("The file wasn't found")

# a = "hello my name is krish"
# b = a.split()
# print(b[::-1])

# c = b[::-1]

# print(" ".join(c))
