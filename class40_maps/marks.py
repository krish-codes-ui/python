#subjects and marks
subjects = ["math","science","english","History","Engineering","Music","Physical education"]
marks = []

for i in range(7):
    num = int(input("Enter mark : "))
    marks.append(num)

for j in range(len(subjects)):
    print(j+1,".",subjects[j],"=",marks[j])

print("the total marks : ",sum(marks))