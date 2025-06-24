#also no duplicates
set1 = {1,'hello',False,True,5,6,2,'go','cat','bat',False}

set2 = {1,4,2,3,4,6,4,7,4,3,2,1,2,3,5,3,6,8,5,3,2,4,6,7,5,3,2,1}

#union (|) : combines elements from both sets,removing duplicates
union1 = set1 | set2
print(union1)

#intersection (&) : finds common elements between sets
intersection1 = set1&set2
print(intersection1)

#difference (-) : finds elements that are in the first set but not in the second set, avoiding common entries
difference1 = set1-set2
print(difference1)

#symmetric difference (^) : finds elements that are in either of the sets but no common elements
symmetric1 = set1^set2
print(symmetric1)

