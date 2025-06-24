import random
 
def choose_random_word(word_list):
    return random.choice(word_list)

word_list = ["cat","bat","hat","cap","bam","sat"]
random_word = choose_random_word(word_list)
guessed_word="_"*len(random_word)
counter=0
w_counter=0
while(counter<3 and w_counter<10):
    guess=input("guess a letter-")
    print(guessed_word)
    if guess in(random_word):
        print("you got a word right")
        counter+=1
    else:
        print("Wrong answer")
        w_counter+=1
if(counter==3):
    print("And you have won!!")
else:
    ("Print you have lost your body")