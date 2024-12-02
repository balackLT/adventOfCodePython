import itertools

file = open("input/day2.txt", "r")
lines = [[int(y) for y in x.split()] for x in file.read().splitlines()]

def is_safe(line):
    increasing = all(x < y for x, y in zip(line, line[1:]))
    decreasing = all(x > y for x, y in zip(line, line[1:]))
    diff = all(abs(x - y) <= 3 for x, y in zip(line, line[1:]))
    return diff and (increasing or decreasing)

def is_safe_dampener(line):
    for permutation in itertools.combinations(line, len(line) - 1):
        if is_safe(permutation):
            return True
    return False

safe_count = 0
safe_count_dampener = 0

for line in lines:
    if is_safe(line):
        safe_count += 1
        safe_count_dampener += 1
    elif is_safe_dampener(line): # dampener
        safe_count_dampener += 1

print(safe_count)
print(safe_count_dampener)


