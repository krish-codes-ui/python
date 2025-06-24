counter_1=0
counter_2=0
words=["cat","khvijde","desjek","wall","uhdedq","poster","ujikdm","book","iuw","window","oljk","lock"]
words_2=["cat","khvijde","desjek","wall","uhdedq","poster","ujikdm","book","iuw","window","oljk","lock"]
for word in words:
    counter_1+=1
    for word_2 in words_2:
       counter_2+=1
       if len(word+word_2)<10:
          print(word+word_2)
       if counter_2 ==5 or counter_1 == 5:
          break
a=input("what words can you find.")
if a=="cat"or a=="wall"or a=="poster"or a=="book"or a=="window"or a=="lock":
   print("you have won")



    