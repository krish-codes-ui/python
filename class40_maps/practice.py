#checking if a data is a member in the list or not
things = ['table','desk','blanket','glass','light','door','octopus','animal','mirror','bed']
items = input("Enter things in a room : ")
if items in things:
    print(items,"is one of the things next to me")
else:
    print(items,"is not one of the things next to me")



