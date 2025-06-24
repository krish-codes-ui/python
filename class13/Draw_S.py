size=9
for row in range(size):
    for column in range(size):
        if row==0 or column == 0 and row < size//2 or row == size//2 or row==size-1 or column==size-1 and row>size//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()