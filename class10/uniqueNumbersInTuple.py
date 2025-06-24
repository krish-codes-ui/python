input = (3,5,6,7,6,2,3,4,5)
output =()
for x in input:
    if x not in(output):
        outputlist=list(output)
        outputlist.insert(1,x)
        output=tuple(outputlist)
        

print(output)
