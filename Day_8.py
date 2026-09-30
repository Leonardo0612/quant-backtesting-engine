alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def shifted_word(word, shift, direction):
    result = ""

    if direction == "encode":
        for letter in word:
            if letter not in alphabet:
                result += letter
            else:
                if letter == " ":
                    result +=  " "

                else:
                    position = alphabet.index(letter)
                    shifted_position = (position + shift) % 26
                    result += alphabet[shifted_position]
        print(f"Your encoded word is:\n{result}")

    else:
        for letter in word:
                if letter not in alphabet:
                    result += letter
                else:
                    if letter == " ":
                        result += " "
        
                    else:
                        position = alphabet.index(letter)
                        shifted_position = (position - shift) % 26
                        result += alphabet[shifted_position]
        print(f"Your decoded word is:\n{result}")



should_continue = True
while should_continue:

    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    shifted_word(word = text, shift = shift_amount, direction = encode_or_decode)

    restart = input("Do you want to play again? Type 'yes' or 'no':\n").lower()

    if restart == "no":
        should_continue = False
        print("BYE!!!")