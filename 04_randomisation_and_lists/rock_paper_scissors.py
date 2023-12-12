import random
user_choice = int(input("What do you choose?\nEnter 0 for Rock.\nEnter 1 for Paper.\nEnter 2 for Scissors.\nYour choice: "))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# printing player choices
game_images = [rock, paper, scissors]
if user_choice > 3 or user_choice < 0:
    print("You typed an invalid number, you lose.")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {computer_choice}")
    print(game_images[computer_choice])

    # game rules and logic
    if user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw.")
    else:
        print("You lose.")