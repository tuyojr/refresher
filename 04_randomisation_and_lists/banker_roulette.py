import random

names_string = input("Give me everybody's names, seperated by a comma. \n")
names = names_string.split(", ")

number_of_names = len(names)
index = random.randint(0, number_of_names-1)
who_will_pay = names[index]
print(f'{who_will_pay} is going to buy the meal today!')