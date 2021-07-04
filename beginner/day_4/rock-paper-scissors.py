rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Code start from here
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice >=3 or user_choice <0:
    print("You typed an invalid number, you lose!")
else:
    elements = ["rock", "paper", "scissors"]  
    game_image = [rock, paper, scissors] 

    print(game_image[user_choice])
    user_choice = elements[user_choice]

    computer_choice = random.randint(0, 2)
    print("Computer chose:\n", game_image[computer_choice])
    computer_choice = elements[computer_choice]

    # -------------------------------- draw ------------------------
    if user_choice == computer_choice:
        print("Game draw")
    # -------------------------------- User ------------------------    
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Wins")
    
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Wins")
        
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Wins")
    # -------------------------------- computer ------------------------    
    elif user_choice == "scissors" and computer_choice == "rock":
        print("You lose!")
        
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lose!")

    elif user_choice == "rock" and computer_choice == "paper":
        print("You lose!")
    