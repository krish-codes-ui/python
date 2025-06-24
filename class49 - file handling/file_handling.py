# r = read
# a = append
# w = Write
# x = create

file = open('file.txt','r') 
print(file.read())
file.close()

file = open('file.txt','rb') 
print(file.read())
file.close()

file = open('file.txt','a') 
file.write("krish")
file.close()

file = open('file.txt','a') 
file.write("krish")
file.close()  

