lines = open("input/day4.txt", "r").read().splitlines()

def get_value_safe(lines, x, y):
    if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[y]):
        return '.'
    return lines[y][x]

def check_combo(lines, x, y, dx, dy):
    combo = (
            get_value_safe(lines, x + dx, y + dy) +
            get_value_safe(lines, x + 2 * dx, y + 2 * dy) +
            get_value_safe(lines, x + 3 * dx, y + 3 * dy)
    )
    return combo == "MAS"

xmas_cnt = 0

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == 'X':
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                          (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in directions:
                if check_combo(lines, x, y, dx, dy):
                    xmas_cnt += 1

print(xmas_cnt)

mas_cnt = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == 'A':
            combo1 = get_value_safe(lines, x - 1, y - 1) + 'A' + get_value_safe(lines, x + 1, y + 1)
            combo2 = get_value_safe(lines, x - 1, y + 1) + 'A' + get_value_safe(lines, x + 1, y - 1)
            if (combo1 == "SAM" or combo1 == "MAS") and (combo2 == "SAM" or combo2 == "MAS"):
                mas_cnt += 1

print(mas_cnt)

