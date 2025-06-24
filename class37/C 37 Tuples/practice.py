#have lists and tuple try append and other functions
Tuples =  ("Kevin","Karen","Jim","Oscar","Toby","Toby")
print(Tuples)
lists = ["Kevin","Karen","Jim","Oscar","Toby","Toby"]
print(lists)

lists2 = lists.copy()
# Tuples2 = Tuples.copy()
lists.extend("hello")
# Tuples.extend("what")
lists.append("Creed")
# Tuples.append("Creed")
lists.insert(1,"Kelly")
# Tuples.insert(1,"Kelly")
lists.remove("Kelly")
# Tuples.remove("Kelly")
lists.clear()
# Tuples.clear()
lists.pop(2)
print(lists)
# Tuples.pop()
lists.sort()
# Tuples.sort()
lists.reverse()
# Tuples.reverse()
print(lists.index("Karen"))
print(Tuples.index("Kevin"))
print(lists.count("Toby"))
print(Tuples.count("Toby"))
#Tuples
coordinates = (4,5)
print(coordinates[0])
#Tuple is immutible and used for special situations
#lists is mutable and will be used a lot


# append()	Adds an element at the end of the lists
# clear()	Removes all the elements from the lists
# copy()	Returns a copy of the lists
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a lists (or any iterable), to the end of the current lists
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the lists
# sort()	Sorts the lists