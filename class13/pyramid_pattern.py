size=9
for row in range(size):
    for column in range(size):
        if row==size-1 or column==1 and row==size-2 or column == 2 and row==size-3 or column == 3 and row==size-4 or column == 4 and row==size-5 or column == 5 and row==5 or column == 6 and row==size-3 or column == 7 and row==size-2 or column == 8 and row==size-1 or column==2 and row==7 or column==3 and row==7 or column==4 and row==7 or column==5 and row==7 or column==6 and row==7 or column==3 and row==6 or column==4 and row==6 or column==5 and row==6 or column==4 and row==5:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()


