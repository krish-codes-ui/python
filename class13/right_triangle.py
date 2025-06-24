#size=8
#for row in range(size):
 #   for column in range(size):
  #      if column==0 or row==size-1 :
   #         print("*",end=' ')
    #    else:
     #       print(" ",end=' ')
    #print()
n = 5
for i in range( n):
    for j in range( i+1):
        print("*", end=" ")
    print()

            