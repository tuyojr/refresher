print("Welcome to the Love Calculator!")
name1 = input("What is your name \n")
name2 = input("What is their name? \n")

lovers = (name1 + name2).lower()
true = str(lovers.count("t") + lovers.count("r") + lovers.count("u") + lovers.count("e"))
love = str(lovers.count("l") + lovers.count("o") + lovers.count("v") + lovers.count("e"))
score = int(true + love)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")