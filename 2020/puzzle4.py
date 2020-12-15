
def create_PartIPassport(passport_list: list) -> list:
    passport_text = []
    passports = []
    for i in range(len(passport_list)):
        if passport_list[i] == '\n':
            passports.append(passport_text)
            passport_text = [] 
        elif i == (len(passport_list) - 1):
            passport_items = [x.strip() for x in passport_list[i].split(' ')]
            passport_text += passport_items
            passports.append(passport_text)
        else:
            passport_items = [x.strip() for x in passport_list[i].split(' ')]
            passport_text += passport_items
    return passports

# Part I
def check_passport(passport: list) -> bool:
    if len(passport) < 7:
        return False
    elif len(passport) == 7:
        check_cid = sum('cid:' in i for i in passport)
        return not check_cid
    else:
        return True

# Part II 

def convert_passport(passport: list) -> dict:
    passport_dict = {}
    for field in passport:
        field_name, field_value = field.split(':')
        passport_dict[field_name] = field_value
    
    return passport_dict

def evaluate_passport(passport: dict) -> bool:
    valid_fields = 0
    birth_year = int(passport['byr'])
    issue_year = int(passport['iyr'])
    exp_year = int(passport['eyr'])
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if birth_year >= 1920 and birth_year <= 2002:
        valid_fields += 1
    if issue_year >= 2010 and issue_year <= 2020:
        valid_fields += 1
    if exp_year >= 2020 and exp_year <= 2030:
        valid_fields += 1
    if passport['hgt'][-2:] == 'cm':
        if int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193:
            valid_fields += 1
    if passport['hgt'][-2:] == 'in':
        if int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76:
            valid_fields += 1
    if passport['hcl'][0] == '#' and len(passport['hcl'][1:]) == 6:
        valid_fields += 1
    if passport['ecl'] in valid_ecl:
        valid_fields += 1
    if len(passport['pid']) == 9:
        valid_fields += 1

    if valid_fields == 7:
        return True
    else:
        return False 
    
if __name__ == '__main__':
    with open("./puzzle4_input.txt", "r") as f:
        passport_list = [i for i in f.readlines()]
    passports = create_PartIPassport(passport_list)
    valid_passports = []
    for passport in passports:
        if check_passport(passport):
            valid_passports.append(passport)
    print("Part I: ", len(valid_passports))

    correct_passports = 0
    for passport in valid_passports:
        passport_dict = convert_passport(passport)
        correct_passports += int(evaluate_passport(passport_dict))
    
    print("Part II: ", correct_passports)
