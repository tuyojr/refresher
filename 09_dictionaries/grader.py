student_scores = {
    "Sherlock": 97,
    "Santan": 80,
    "Brent": 73,
    "Rakim": 81,
    "Cole": 91,
    "Isaiah": 70
}

student_grades = {}

"""
91 - 100 ---> Outstanding
81 - 90 ---> Exceeds Expectation
71 - 80 ---> Acceptable
70 - lower ---> Fail
"""

for student in student_scores:
    score = student_scores[student]

    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[student] = "Exceeds Expectation"
    elif score >= 71 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)