list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max = list_numbers[0]
max_number = 0
last = list_numbers[-1]
for i, ii in enumerate(list_numbers):
    a = ii
    if a >= max:
        max = a
        max_number = i
cnange = list_numbers[max_number]
list_numbers[max_number]=last
list_numbers[-1]=cnange


print(list_numbers)