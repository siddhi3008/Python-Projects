"""
Workflow
1) Input from user(rock, paper, scissor)
2) Computer choice(computer will choose randomly not conditionally)
3) Result print with description


Cases:

A- Rock

Rock Rock = tie

Rock Paper = Paper win

Rock scissor Rock wine


B- Paper

Paper Paper = tie

Paper Rock = Paper win

Paper Scissor = Scissor win


C- Scissor

Scissor Scissor = tie

Scissor Rock = Rock win

Scissor Paper = Scissor win

"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both Chooses same: = Match Tie")
    
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock = Computer win") 

    else:
        print("Rock smashes Scissor = You Win")       
        
elif user_choice =="Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer Win")

    else:
        print("Paper Covers Rock, You Win")

elif user_choice =="Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You Win")

    else:
        print("Rock smashes Scissor , Computer Win")
