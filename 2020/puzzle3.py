import math

with open('./puzzle3_input.txt', 'r') as f:
    slope_map = [i.strip() for i in f.readlines()]
height = len(slope_map)
max_width = height * 7
n_pattern = math.ceil(max_width/31)

full_map = [i * n_pattern for i in slope_map]

def get_trees(full_map: list, right: int, down: int) -> int:
    trees = 0
    position = 0
    for i in range(0, len(full_map), down):
        if full_map[i][position] == '#':
            trees += 1
        position += right

    return trees

tree11 = get_trees(full_map, 1, 1)
tree31 = get_trees(full_map, 3, 1)
tree51 = get_trees(full_map, 5, 1)
tree71 = get_trees(full_map, 7, 1)
tree12 = get_trees(full_map, 1, 2)

answer = tree11 * tree31 * tree51 * tree71 * tree12

print(answer)





