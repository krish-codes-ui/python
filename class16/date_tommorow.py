year = int(input("what is the year"))
month = int(input("what is the month"))
day = int(input("what is the day"))
if day==31:
    day=1
else:
    day+=1
print("tommorow is ",year,"-",month,"-",day)