#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

for names in open("Day 24/Main/Input/Names/invited_names.txt"):
    names_stripped = names.strip()

    with open("Day 24/Main/Input/Letters/starting_letter.txt", mode = "r") as letter:
        contents = letter.read()
        replaced_letter = contents.replace("[name]", names_stripped)

        with open(f"Day 24/Main/Output/ReadyToSend/letter_for_{names_stripped}.txt", mode = "w") as letter:
            letter.write(replaced_letter)
