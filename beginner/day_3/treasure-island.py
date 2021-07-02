print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
step1 = input("You're are at a sea beach. Where you want to go? Type 'left' or 'right'\n").lower()

if step1 == "left":
    step2 = input("You came to a lake stuck. There is an island in the middle of the lake. Type 'wait' to wait for a boat. or type 'swim' to swim across.\n").lower()
    if step2 == "wait":   
        step3 = input("You want to go to market but it's raining outside. Type 'wait' to until the rain stop, type 'umbrella' to use umbrella to go outside or type 'later' to go later\n").lower()
        if step3 == "wait" or step3 == "later":
            print("You win the game congratulations!!!")
        else:
            print("Game over! Thander fall on you and you die!")
    else:
        print("Game over! a shark eats you!")
else:
     print("Game over! You fall in a sand hole")    
    

    