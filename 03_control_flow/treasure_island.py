print('''
      .--..--..--..--..--..--.
    .' \  (`._   (_)     _   \
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\
             ||       ||
              ||_.-.   ||_.-.
            (_.--__) (_.--__)
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()


if direction == "right":
    print("You fell into a hole. Game Over!")
elif direction == "left":
    cross_lake = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat.Type 'swim' to swim across. \n").lower()
    if cross_lake == "swim":
        print("You got attacked by a Trout. Game Over!")
    elif cross_lake == "wait":
        island_door = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()
        if island_door == "red":
            print("You fell into a pit of fire and got burned. Game Over!")
        elif island_door == "yellow":
            print("Congratulations! You found the reasure! You won!")
        elif island_door == "blue":
            print("You got eaten by beasts! Game Over!")
        else:
            print("Invalid Input! Game Over!")
    else:
        print("Invalid Input! Game Over!")
else:
    print("Invalid Input! Game Over!")