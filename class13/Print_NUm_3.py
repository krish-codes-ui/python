size=7
for row in range(size):
    for column in range(size):
        if column == size-1 or row==0 or row == size//2 or row==size-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    
