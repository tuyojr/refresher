print("Welcome  to the tip calculator.")
total = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip = (total / number_of_people) * (1 + (percentage_tip/100))
each_person_tip = 0

if percentage_tip == 10:
    each_person_tip += tip
elif percentage_tip == 12:
    each_person_tip += tip
elif percentage_tip == 15:
    each_person_tip += tip

print(f'Each person should pay: ${round(each_person_tip, 2)}')