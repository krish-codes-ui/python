import tkinter as tk


screen = tk.Tk()
screen.geometry("500x500")
# size of the screen

screen.title("tk ------------")
# title of the application

text = tk.StringVar()
text.set("My name is krish")
# get the text on the screen
label = tk.Label(screen,textvariable=text,justify=tk.LEFT,bg="blue",height=2,width=15,fg="white",bd=5,padx=50,pady=50)
# label = tk.Label(screen,textvariable=text,anchor=tk.CENTER,bg="lightblue",height=3,width=30,bd=3,font=("Arial", 16, "bold"),fg="red",padx=15,pady=15,justify=tk.CENTER,relief=tk.RAISED,underline=0,wraplength=250 )
# label sets the qualities like color and size of text
label.pack()
#label.pack packs up everything inside a pack and puts that into the screen

screen.mainloop()                      

