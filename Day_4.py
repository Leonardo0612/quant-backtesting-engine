import random

rock_paper_scissors = ["Rock", "Paper", "Scissors"]

human_choice = int(input("What do you choose? Type 0 for 'Rock', type 1 for 'Paper', type 2 for 'Scissors': "))

bot_choice = random.randint(0, 2)
# 0 = Rock
# 1 = Paper
# 2 = Scissors

print("Bot chooses " + rock_paper_scissors[bot_choice])

result = (human_choice - bot_choice) % 3

if result == 0:
    print("Yout tie!")

elif result == 1:
    print("You win!")

else:
    print("You lose!")





# WIN  0 and 2   1 and 0   2 and 1
# LOSE 0 and 1   1 and 2   2 and 0