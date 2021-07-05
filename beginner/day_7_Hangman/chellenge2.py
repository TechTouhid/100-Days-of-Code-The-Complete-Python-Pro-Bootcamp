import random

# Step 2
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Test the code
print(f"Pass: the solution is {chosen_word}")
# TODO-1 - Create a empty list called display. For each letter in the chosen_word, add a "_" to 'display'. So if the
# chosen_word was "apple", display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess
display = []
for letter in chosen_word:
    display.append("_")
print(display)

guess = input("Guess a letter!\n").lower()
# TODO-2 - Loop through each position in the chosen_word
# If the letter at the position matches 'guess' then reveal that letter in the display at that position
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","p","_","_"].


for position in range(len(chosen_word)):
    if guess == chosen_word[position]:
        display[position] = guess

# TODO-3 - Print 'display' and you should see the guessed letter in the correct position and every other letter
#  replace with "_". Hint - don't worry about getting the user to guess next letter. we'll tackle the in step 3
print(display)
