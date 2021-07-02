print("Welcome to rollercoster")
height  = int(input("What is your height in cm?"))

bill = 0

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <=18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 15
        print("Please pay $12")
    wants_photo = input("Do you want to photo taken? Y or N ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your total bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

