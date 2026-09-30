keep_playing = True

players = {}

print("Welcome to the bid game!")

while keep_playing == True:
    name = input("What is your name?\n")
    bid = input("What is your bid?\n£")
    other_players = input("Are there other bidders? Type 'yes' or 'no'\n").lower()

    players[name] = bid

    if other_players == "yes":
        print("\n" * 100)
    else:
        keep_playing = False

print("\n" * 100)

highest_bid = 0
winner = ""

for name in players:
    bid = int(players[name])

    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"The highest bidder is {winner} with a bid of £{highest_bid}")