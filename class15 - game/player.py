size=5
row2=2
column2=2
for i in range(size+1) :
    for row in range(size):
        for column in range(size):
            if row==row2 and column2==column:
                print("p",end=' ')
            else:
                print("*",end=' ')
        print()
    user_input=input("Say w or a or s or d")

    if user_input=="w":
        row2-=1
    elif user_input=="a":
        column2-=1

    elif user_input=="s":
        row2+=1
    elif user_input=="d":
        column2+=1
    else:
        print("you have picked the wrong one")

