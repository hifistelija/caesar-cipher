alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
            continue
            
        old_index = alphabet.index(letter) 
        if cipher_direction == "encode":
            new_index = (old_index + shift_amount) % 26
        elif cipher_direction == "decode":
            new_index = (old_index - shift_amount) % 26
            
        new_letter = alphabet[new_index]
        end_text += new_letter
    print(f"The {cipher_direction}d text is: {end_text}")    


def get_input():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    return direction, text, shift


from art import logo
print(logo)

start_program = True

while start_program:
    direction, text, shift = get_input()
    caesar(text, shift, direction)
    start_program = input("Do you want to start the program again? Type 'yes' or 'no':\n")
    if start_program.lower() == "no":
        start_program = False
        print("Goodbye")
    else:
        start_program = True
