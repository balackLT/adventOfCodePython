from collections import defaultdict

def validate_update(update, deps):
    seq = set()
    for num in update:
        prereq = deps[num].intersection(update)
        if prereq.issubset(seq):
            seq.add(num)
        else:
            return False

    return True

def sort_update(update, deps):
    relevant_deps = {num: deps[num].intersection(update) for num in update}
    sorted_update = [x[0] for x in sorted(relevant_deps.items(), key = lambda n: len(n[1]))]
    return sorted_update

input = open("input/day5.txt", "r").read().split("\n\n")
rules = [line.split('|') for line in input[0].splitlines()]
updates = [line.split(',') for line in input[1].splitlines()]

dependencies = defaultdict(set)
for depends_on, num in rules:
    dependencies[num].add(depends_on)

result1, result2 = 0, 0
for update in updates:
    if validate_update(update, dependencies):
        middle_index = len(update) // 2
        result1 += int(update[middle_index])
    else:
        sorted_update = sort_update(update, dependencies)
        middle_index = len(sorted_update) // 2
        result2 += int(sorted_update[middle_index])

print(result1)
print(result2)
