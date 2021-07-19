import random

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

if difficulty_level == 'easy':
    attempts = 10
else:
    attempts = 5

number = random.randint(1, 101)
number_guessed = True
while number_guessed:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess < number:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
    elif guess > number:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number} ")
        number_guessed = False
    if attempts == 0:
        print("You have run out of guess you lose!!")
        number_guessed = False

