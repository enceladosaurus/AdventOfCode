with open("./puzzle7_input.txt", "r") as f:
    rule_file = [i.strip() for i in f.readlines()]

# Part I
def check_bags(rule_file: list, bag: str) -> list:
    bags_found = []
    for rule in rule_file:
        rule_list = rule.split("contain")
        if bag in rule_list[1]:  
            bags_found.append(rule_list[0][:-6])
            bags_found.extend(check_bags(rule_file, rule_list[0][:-6]))

    return bags_found

# Part II
rulebook = {}
for rule in rule_file:
    rule_list = rule.split("contain")
    container_bag = rule_list[0][:-6]
    contains = [i.strip() for i in rule_list[1].replace('.', '').replace('bags', '').replace('bag', '').split(',')]
    rulebook[container_bag] = contains

def count_bags(rulebook: dict, bag: str) -> int:
    number_of_bags = 0
    child_bags = rulebook[bag]
    if child_bags == ['no other']:
        return 0
    else:
        bag_value = sum(int(bag[:2]) + int(bag[:2]) * count_bags(rulebook, bag[2:].strip()) for bag in child_bags)
        number_of_bags += bag_value
    return number_of_bags

if __name__ == '__main__':
    found_list = check_bags(rule_file, "shiny gold")
    print("Part 1: ", len(set(found_list)))
    print("Part 2: ", count_bags(rulebook, "shiny gold"))
    
