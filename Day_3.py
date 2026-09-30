print("Welcome to treasure island!")
print("Your mission is to find the treasure.")

direction = input("You're at a cross road. Where do you wanna go? Type 'left' or 'right': ").lower()

if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()

    if swim == "wait":
        print("Nice! You made it across")
        bear = input("Do you want to chill with the bear, run away from the bear, or kill the bear. Type 'chill', 'run' or 'kill': ").lower()

        if bear == "chill":
            print("Niceee, you found the treasure!")

        else:
            print("lol. You died at the end")

    else:
        print("lol. You drowned")

else:
    print("You have died. lol")