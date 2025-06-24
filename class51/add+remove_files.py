def create_file(x):
    file = open(f"water_bottle{x}.txt",'a')
    # a is append
    file.close()

import os
for x in range(100):
    os.remove(f"water_bottle{x}.txt")