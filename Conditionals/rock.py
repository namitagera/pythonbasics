
import random 

choice = random.choice(["rock","paper", "scissors"])
comp_choice = choice
user_choice = input("Do you want a rock paper or scissors?")

print("Computer choice " + choice)

if comp_choice == user_choice:
    print("TIE") 
elif comp_choice == "scissors" and user_choice == "rock":
    print("You win")
elif comp_choice == "rock" and user_choice == "paper":
    print("You win")
elif comp_choice == "paper" and user_choice == "scissors":
    print("You win")
else:
    print("Computer wins")