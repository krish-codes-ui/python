# for x in range(101):
#     create_file(x)


import heroes

for x in range(11):
    name = heroes.gen()
    open(f"{name}.txt",'a')


