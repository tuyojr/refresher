row1 = ['💼', '💼', '💼']
row2 = ['💼', '💼', '💼']
row3 = ['💼', '💼', '💼']
map = [row1, row2, row3]

print("    1\t  2\t3")
print(f'1{row1}\n2{row2}\n3{row3}')

position = input("Where do you want to put the treasure? Enter the matrix e.g 23 (column 2, row 3)\nValue: ")

column = int(position[0]) -1
row = int(position[1]) - 1
map[column][row] = 'X'

print("\n**************************************************************************************\n")
print("Your treasure spot has been marked!")
print("    1\t  2\t3")
print(f'1{row1}\n2{row2}\n3{row3}')