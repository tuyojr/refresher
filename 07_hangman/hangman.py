import art
import random
import word_list

art

random_word = random.choice(word_list.word_list).lower()
word_length = len(random_word)

display_blanks = []

for character in range(word_length):
    display_blanks.append('_')

print(f"The word is {len(display_blanks)} characters long.")
print(' '.join(display_blanks))
print('\n')

lives = 6
stage_count = -1

end_of_game = False

while lives > 0 and not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    if user_guess == 'exit':
        break

    if user_guess in display_blanks:
        print(f"You already guessed '{user_guess}'")

    if user_guess not in random_word:
        print(f"'{user_guess}' is not in the word, you lose a chance.")
        lives -= 1
        stage_count += 1
        print(art.stages[stage_count])
        print(f"\nChance(s) left: {lives}.")
        
    else:
        for position in range(word_length):
            letter = random_word[position]
            if letter == user_guess:
                display_blanks[position] = letter

    print('\n')
    print(' '.join(display_blanks))
    print('\n')

    if '_' not in display_blanks:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game == True
        print(f"The word was {random_word}")
        print("Sorry you lose.")