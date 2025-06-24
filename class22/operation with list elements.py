#Changing list elements
my_list = [1,3,5,7,9,11]
print("List of odd numbers : ")
for a in my_list:
    print(a)
my_list[0:6]=2,4,6,8,10,12
print("List of even numbers : ")
for b in my_list:
    print(b)

#Adding more elements in a list
my_list1 = [1,5,7,3,9]
my_list1.append(8)
print(my_list1)
my_list1.extend([3,5,6,7,6,5,32])
print(my_list1)

# inserting elements in the list
my_list2 = [2,"xh",6,"kefj",9,"dj",5,"ij",7,"kfh","wfkjb","ukrh"]
print(my_list2)
my_list2.insert(6,"ilwefjkfwejl")
my_list2.insert(2,"hello")
my_list2.insert(9,7456)
my_list2.insert(4,"okokok")
print(my_list2)