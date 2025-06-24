class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    
    def __str__(self):
        # The function will return a string
        return self.word + '(' + self.meaning + ')'

flash = []
print("Welcome to the flashcard application")

#The following loop will be repeated until the user stops to add the flashcards
while(True):
    word = input("Enter the flashcard name : ")
    meaning = input("Enter the meaning of the word : ")
    flash.append(flashcard(word,meaning))

    option = int((input("Enter 0 if you want to add another flashcard : ")))
    if(option):
        break

# printing all of the flashcards
print("\n Your flashcards : ")
for i in flash : 
    print("@#$>",i)