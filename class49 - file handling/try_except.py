while 0<1:
    try : 
        value = int(input("Enter a number : "))
        if value < 0 :
            print("Your value is negative, try again")
        else:
            print("Your value is positive, good job")
            break
    except ValueError :     
        print("value is not a number")   
        print("please try again") 

