student_heights = input("Input a list of student heights in cm:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
number_of_students = 0
for height in student_heights:
    total_height += height
    number_of_students += 1
average_height = round(total_height/number_of_students)
print(f"The average height is: {average_height} cm")
