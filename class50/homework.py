def read_display(file):
    file_name = open(f'{file}','r') 
    print(file_name.read())
    file_name.close()
file='poem.txt'
read_display(file)
