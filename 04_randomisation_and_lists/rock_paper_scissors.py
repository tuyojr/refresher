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
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)
computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

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