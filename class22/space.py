space_counter=0
user = input("give me a string-")
for letter in user:
    if letter == " ":
        space_counter+=1
print("You have",space_counter,"spaces")