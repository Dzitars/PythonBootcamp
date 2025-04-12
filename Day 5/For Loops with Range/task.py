total_number = 0

#range includes lower number, not the higher one. Would need to be range(1,101) to go up to 100
for number in range(1,101):
    total_number += number

print(f"{total_number}")