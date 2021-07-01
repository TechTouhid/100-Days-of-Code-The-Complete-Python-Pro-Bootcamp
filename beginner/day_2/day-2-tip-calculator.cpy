# If the bill was $150.00, split between 5 people, with 13% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal place = 33.60

print("Welcome to the tip calculator.\n")
total_bitll  = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_person = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * total_bitll + total_bitll
print(f"Each persona should pay: ${bill_with_tip/total_person:.2f}")