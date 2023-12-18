import math

def paint_calc(height, width, cover):
    result = math.ceil((height * width) / cover)
    print(f"You'll need {result} cans of paint.")

test_h = int(input("Height of wall (in meters): "))
test_w = int(input("Width of wall (in meters): "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)