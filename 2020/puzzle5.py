with open('./puzzle5_input.txt', 'r') as f:
    pass_list = [i.strip() for i in f.readlines()]


'''
def find_row(row_string: str):
    current_rows = [0, 128]
    for i in range(6):
        half = (current_rows[1] - current_rows[0]) / 2
        if row_string[i] == 'F':
            current_rows[1] = current_rows[0] + half
        else:
            current_rows[0] = current_rows[1] - half
        
    if row_string[6] == 'F':
        return current_rows[0]
    else:
        return current_rows[1]

def find_column(col_string: str):
    current_columns = [0, 8]
    for i in range(7, 10):
        half = (current_columns[1] - current_columns[0]) / 2
        if col_string[i] == 'L':
            current_columns[1] = current_columns[0] + half
        else:
            current_columns[0] = current_columns[1] - half
    
    if col_string[9] == 'L':
        return current_columns[0]
    else:
        return current_columns[1] - 1
'''
seat_id = []
for bp in pass_list:
    row = find_row(bp)
    column = find_column(bp)
    seat_id.append((row * 8) + column)

print(max(seat_id))


# multiply row by 8 and add column
