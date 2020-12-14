
def convert(string: str) -> str:
    converted_string = string.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

    return converted_string

def get_id(row: int, column: int) -> int:

    return (row * 8) + column

def find_missing_seat(seat_ix: list, n_seats: int) -> list:
    missing_seats = [seat for seat in range(min(seat_ix), max(seat_ix)) if seat not in seat_ix]

    return missing_seats
    
if __name__ == '__main__':
    with open('./puzzle5_input.txt', 'r') as f:
        pass_list = [i.strip() for i in f.readlines()]

    # Part I    
    seat_ix = []

    for bpass in pass_list:
        converted_pass = convert(bpass)
        row = int(converted_pass[:7], 2)
        column = int(converted_pass[7:], 2)

        seat_ix.append(get_id(row, column))

    print(max(seat_ix))

    # Part II

    rows = 128
    cols = 8
    n_seats = rows * cols

    print(find_missing_seat(seat_ix, n_seats))