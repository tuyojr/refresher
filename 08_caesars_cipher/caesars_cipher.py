import art

art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

def caesar(input_text, shift_amount, cipher_direction):

        output = ''

        # for position in range(len(palin_text)):
        #     letter = palin_text[position]
        #     for index in range(len(alphabet)):
        #         char = alphabet[index]
        #         if letter == char:
        #             new_position = index + shift_amount
        #             shifted = alphabet[new_position]
        #             encoded_text += shifted
        
        if cipher_direction == 'decode':
            shift_amount *= -1

        for charcater in input_text:
            if charcater in alphabet:
                position = alphabet.index(charcater)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                output += new_letter
            else:
               output += charcater
        print(f'The {cipher_direction}d text is {output}.\n')

go_again = True

while go_again:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)

    caesar(text, shift, direction)

    keep_going = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")

    if keep_going == 'no':
        go_again = False
        print('Goodbye!')