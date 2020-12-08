with open("./puzzle4_input.txt", "r") as f:
    passport_list = [i for i in f.readlines()]
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

if __name__ == '__main__':
    valid_passports = 0
    for passport in passports:
        valid_passports += int(check_passport(passport))
    print("Part I: ", valid_passports)
