the_n = int(input(''))

start_from: int = the_n + 1 # this is the amount of progress we should have one each row
second_half: bool = False
row_number: int = 1

for current_row in range((2 * the_n) + 1):
    this_line = ''
    this_line += " " * start_from
    this_line += "*" * ((2 * row_number) - 1)
    if second_half or row_number == the_n + 1:
        row_number -= 1
        start_from += 1
        second_half = True
        if not row_number:
            print(this_line) 
            break
    else:
        row_number += 1
        start_from -= 1
    
    print(this_line)

