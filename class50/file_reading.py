try:
    file = open("tat.txt",'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print("The file is not found")
    