player_one_paper=False
player_one_rock=False
player_one_scissors=False
player_two_paper=False
player_two_rock=False
player_two_scissors=False
name_1=input("what is your name")
name_2=input("what is your name")
input_1 = input("you are player one , choose rock ,papers ,or scissors-")
input_2 = input("you are player two , now you choose rock ,papers ,or scissors-")
if input_1 == "paper":
    player_one_paper=True

if input_1 == "rock":
    player_one_rock=True

if input_1 == "scissors":
    player_one_scissors=True
#################################
if input_2 == "paper":
    player_two_paper=True

if input_2 == "rock":
    player_two_rock=True

if input_2 == "scissors":
    player_two_scissors=True
##################################
if player_one_paper==True and player_two_paper==True:
    print("draw")
if player_one_paper==True and player_two_rock==True:
    print(name_1+" wins")
if player_one_paper==True and player_two_scissors==True:
    print(name_2+" wins")
if player_one_rock==True and player_two_paper==True:
    print(name_2+" wins")
if player_one_rock==True and player_two_rock==True:
    print("draw")
if player_one_rock==True and player_two_scissors==True:
    print(name_1+" wins")
if player_one_scissors==True and player_two_paper==True:
    print(name_1+" wins")
if player_one_scissors==True and player_two_rock==True:
    print(name_2+" wins")
if player_one_scissors==True and player_two_scissors==True:
    print("draw")




