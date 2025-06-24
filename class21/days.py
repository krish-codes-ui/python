def md():
    days=int(input("how many days"))
    months=days//30
    d = days%30
    print("you have ",months,"months and ",d,"days")
md()