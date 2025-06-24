# List of all suits
suits=['Heart','Spade','Clover','Diamond']

# List of all ranks
Ranks = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']

# Matching all suits with all ranks
for rank in Ranks:
    for suit in suits:
        print(f'{rank} of {suit}'.ljust(16), end='')

    print()

    