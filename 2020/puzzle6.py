def clean_answers(answer_list: list) -> list:
    answer_text = ''
    answers = []
    for i in answer_list:
        if i == '\n':
            answers.append(answer_text)
            answer_text = ''
        else:
            answer_text += i.strip()
    return answers

def create_answer_groups(answer_list: list) -> list:
    grouped_answers = []
    group = []

    for i in answer_list:
        if i == '\n':
            grouped_answers.append(group)
            group = []
        else:
            group.append(i.strip())
    
    return grouped_answers

def find_common_answers(answers: list) -> list:
    possible_answers = list(set(''.join(answers)))
    total_answer = ''.join(answers)
    common_answers = [i for i in possible_answers if total_answer.count(i) == len(answers)]

    return common_answers
    
if __name__ == '__main__':
    with open('./puzzle6_input.txt', 'r') as f:
        answer_list = [i for i in f.readlines()]
    
    # Part I
    answers = clean_answers(answer_list)
    counts = sum([len(set(answer)) for answer in answers])
    print(counts)

    # Part II

    grouped_answers = create_answer_groups(answer_list)
    common_answers = []
    for group in grouped_answers:
        common_answers += find_common_answers(group)
    
    print(len(common_answers))