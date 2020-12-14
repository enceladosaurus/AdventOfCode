# Part I

def find_break(instruction_list: list) -> int:
    accumulator = 0
    instructions_completed = []
    i = 0

    while i < len(instruction_list):
        
        instruction = instruction_list[i]
        value = int(instruction[4:])

        if i in instructions_completed:
            return accumulator

        elif instruction[:3] == 'acc':
            accumulator += value
            instructions_completed.append(i)
            i+= 1
        elif instruction[:3] == 'jmp':
            instructions_completed.append(i)
            i = i + value 
        else:
            instructions_completed.append(i)
            i += 1
    
    return accumulator


# Part II 

def test_game(instruction_list: list):

    accumulator = 0
    instructions_completed = []
    i = 0
    jumps = []

    while i < len(instruction_list):
        
        instruction = instruction_list[i]
        value = int(instruction[4:])

        if i in instructions_completed:
            return True, accumulator

        elif instruction[:3] == 'acc':
            accumulator += value
            instructions_completed.append(i)
            i+= 1
        elif instruction[:3] == 'jmp':
            instructions_completed.append(i)
            jumps.append(i)
            i = i + value 
        else:
            instructions_completed.append(i)
            i += 1
    
    return False, accumulator

def fix_game(instruction_list: list) -> int:

    broken = True
    possibles = []
    instructions_tested = []
    test_list = instruction_list.copy()
    
    for i in range(len(instruction_list)):
        if instruction_list[i][:3] == 'jmp' or instruction_list[i][:3] == 'nop':
            possibles.append(i)

    while broken:
        
        poss_to_test = [i for i in possibles if i not in instructions_tested]
        test = poss_to_test[0]

        if test_list[test][:3] == 'jmp':
            test_list[test] = test_list[test].replace('jmp', 'nop')
        else:
            test_list[test] = test_list[test].replace('nop', 'jmp')

        instructions_tested.append(test)
        broken, accumulator = test_game(test_list)
        test_list = instruction_list.copy()

    return accumulator


if __name__ == '__main__':
    
    with open('./puzzle8_input.txt') as f:
        instruction_list = [i.strip() for i in f.readlines() if i != '\n']

    # Part I
    print(find_break(instruction_list))
    # Part II
    print(fix_game(instruction_list))