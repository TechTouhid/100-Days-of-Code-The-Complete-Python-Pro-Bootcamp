from art import logo
print(logo)
print("Welcome to the secret auction program!")

auction_dict = {}
ask_for_bid = True

while ask_for_bid:
    name = input("What is your name?: ")
    bid = int(input("What's your bid? : $"))
    auction_dict[name] = bid
    ask = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    if ask == 'no':
        ask_for_bid = False

winner = {
    "name": '',
    "winner_bid": 0
}
for bid in auction_dict:
    temp_bid = auction_dict[bid]
    if winner["winner_bid"] <= temp_bid:
        winner["winner_bid"] = temp_bid
        winner["name"] = bid

print("The winner is " + winner["name"] + " with a bid of $" + str(winner["winner_bid"]))