password=input("try a password")
while 'a'  not in(password) and 'b'  not in(password)and 'c'  not in(password)and 'd'  not in(password)and 'e'  not in(password)and 'f'  not in(password)and 'g'  not in(password)and 'h'  not in(password)and 'i'  not in(password)and 'j'  not in(password)and 'k'  not in(password)and 'l'  not in(password)and 'm'  not in(password)and 'n'  not in(password)and 'o'  not in(password)and 'p'  not in(password)and 'q'  not in(password)and 'r'  not in(password)and 's'  not in(password)and 't'  not in(password)and 'u'  not in(password)and 'v'  not in(password)and 'w'  not in(password)and 'x'  not in(password)and 'y'  not in(password)and 'z'  not in(password):
   print("you need letters in your password-")
   password=input("try password again")
print("you passed the first part")

while '1' not in(password) and '2' not in(password) and '3' not in(password) and '4' not in(password) and '5' not in(password) and '6' not in(password) and '7' not in(password) and '8' not in(password) and '9' not in(password):
   print("you need numbers in your password")
   password=input("try password again-")
print("you passed the second part")

while len(password)<=8:
   print("Your password needs to be longer than 8 characters")
   password=input("try password again-")
print("youre done , Good Job")
