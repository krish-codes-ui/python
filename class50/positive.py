# class Negative_Value_Error:
#    pass

# def check_positive(num):
#     try:
#         if num>0:
#             print("It is positive!!")
#     except Negative_Value_Error:
#         print("The value is negative.")
# num = int(input("Enter the number to check for negative : "))
# check_positive(num)

class NegativeValueError(Exception):
    pass
 
def check_positive(num):
    try:
        if (num < 0):
            # negative
            raise NegativeValueError("negative integers are not allowed")
        else:
            print("positive integer")
    except NegativeValueError as e:
        print(f"Error:{e}")
 
num = -10
check_positive(num)