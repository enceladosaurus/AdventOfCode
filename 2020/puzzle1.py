with open("./puzzle1_input.txt", "r") as f:
    expense_report = [int(i.strip()) for i in f.readlines()]
part1_answers = [a * b for a in expense_report for b in expense_report if a + b == 2020]
print(set(part1_answers))

part2_answers = [a * b * c for a in expense_report for b in expense_report for c in expense_report if a + b + c == 2020]
print(set(part2_answers))

