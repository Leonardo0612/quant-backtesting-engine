import random
play = True
print("Welcome to the guessing game!")
print("You have to choose a random number from 1-100")
easy_or_hard = input("Do you want to play easy or hard mode: ").lower()
random_number = random.randint(1, 100)

def hard():
    global guesses
    print(f"You have {guesses} guesses left.")
    guess = int(input("Your guess: "))

    if guess < random_number:
        print("Your guess is too low!")
    elif guess > random_number:
        print("Your guess is too high!")
    else:
        print(f"The number was {random_number}!\nGood Job!")
        return True
    guesses -= 1
    return False

def easy():
    global guesses
    print(f"You have {guesses} guesses left.")
    guess = int(input("Your guess: "))
    
    if guess < random_number:
        print("Your guess is too low!")
    elif guess > random_number:
        print("Your guess is too high!")
    else:
        print(f"The number was {random_number}!\nGood Job!")
        return True
    guesses -= 1
    return False

if easy_or_hard == "easy":
    guesses = 10
    while play and guesses > 0:
        if easy():
            play = False
    if guesses == 0 and play:
        print("LOL, you ran out of guesses!")

elif easy_or_hard == "hard":
    guesses = 5
    while play and guesses > 0:
        if hard():
            play = False
    if guesses == 0 and play:
        print("LOL, you ran out of guesses!")