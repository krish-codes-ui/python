Size = 8
for row in range(Size):
    for column in range(Size):
        if row == 0 or column == Size-1 or row==Size-1 or column ==0 or row == Size//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()        
