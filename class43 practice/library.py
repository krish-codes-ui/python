class library:
    def __init__(self,book_name,author_name):
        self.book_name = book_name
        self.author_name = author_name

    def get_data(self):
        self.book_name=input("What is the book name : ")
        self.author_name=input("What is the author's name : ")
    def display_data(self):
        print(self.book_name,":",self.author_name)
        
        

