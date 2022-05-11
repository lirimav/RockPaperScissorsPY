import random

game = ["Rock", "Paper", "Scissors"]
print()
print("Welcome to Rock Paper Scissors game!")
print("Type exit to exit game.")


while True:
    print()
    player = input("Choose rock, paper or scissors: ").lower()
    nr = random.randint(0, 2)
    computer = game[nr].lower()
    if player == computer:
        print(f"You chose {player}, computer chose {computer}.")
        print("Tie")
    elif player == "rock" and computer == "paper":
        print(f"You chose {player}, computer chose {computer}.")
        print("Computer Wins!")
    elif player == "rock" and computer == "scissors":
        print(f"You chose {player}, computer chose {computer}.")
        print("Player wins!")
    elif player == "paper" and computer == "rock":
        print(f"You chose {player}, computer chose {computer}.")
        print("Player Wins!")
    elif player == "paper" and computer == "scissors":
        print(f"You chose {player}, computer chose {computer}.")
        print("Computer Wins!")
    elif player == "scissors" and computer == "rock":
        print(f"You chose {player}, computer chose {computer}.")
        print("Computer Wins!")
    elif player == "scissors" and computer == "paper":
        print(f"You chose {player}, computer chose {computer}.")
        print("Player Wins!")
    elif player == "exit":
        print("Thanks for playing...")
        break
    else:
        print("Wrong value")