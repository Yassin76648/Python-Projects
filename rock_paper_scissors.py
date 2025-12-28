import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper","scissors"]
while True :
    user_input = input("Type Rock / Paper / Scissors or Q to quit : ").lower()
    if user_input  == "q" :
        break

    if user_input not in  options:
        continue
    
    random_no = random.randint(0,2)
    computer_pick = options[random_no]

    if user_input == "Rock" and computer_pick == "scissors" :
        print("computer pick : " , computer_pick)
        print("You Won !!")
        user_wins += 1
        

    elif user_input == "scissors" and computer_pick == "paper" :
        print("computer pick : " , computer_pick)
        print("You Won !!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock" :
        print("computer pick : " , computer_pick)
        print("You Won !!")
        user_wins += 1
        
    else :
        print("computer pick : " , computer_pick)
        print("You Lost !!")
        computer_wins+=1



print ("You Won ", user_wins , " and the computer Won ", computer_wins)
print ("Goodbye !")