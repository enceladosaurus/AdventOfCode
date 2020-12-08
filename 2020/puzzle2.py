with open("./puzzle2_input.txt", "r") as f:
    password_list = [i.strip() for i in f.readlines()]
pair_list = [(i.split(":")[0], i.split(":")[1].strip()) for i in password_list]

# Part I
def check_password(pair) -> bool:
    rule = pair[0].split(' ')
    password = pair[1]
    letter = rule[1]
    bounds = rule[0].split('-')
    n_letter = password.count(letter)

    if (n_letter >= int(bounds[0])) and (n_letter <= int(bounds[1])):
        return True
    else:
        return False

# Part II
def check_password2(pair) -> bool:
    matches = 0
    rule = pair[0].split(' ')
    password = pair[1]
    letter = rule[1]
    positions = rule[0].split('-')
    converted_positions = [int(i) - 1 for i in positions]

    if (password[converted_positions[0]] == letter):
        matches += 1
    if (password[converted_positions[1]] == letter):
        matches += 1
    
    if matches == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    count = 0
    for pair in pair_list:
        if check_password(pair):
            count += 1
        if check_password2(pair):
            count2 += 1

    print(count)
    print(count2)


