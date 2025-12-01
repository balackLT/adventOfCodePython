import itertools
import time
from itertools import permutations


def main():
    with open("input/day7.txt", "r") as file:
        file_content = file.read().splitlines()

    equations = []
    for line in file_content:
        split = line.split(':')
        target = int(split[0])
        operands = [x for x in split[1].split()]
        equations.append((target, operands))

    result = 0
    for target, operands in equations:
        if evaluate_eq(operands, target):
            result += target

    print(result)


def evaluate_eq(operands, target):
    variations = len(operands) - 1
    combos = [x for x in itertools.product('+*', repeat=variations)]
    for combo in combos:
        permutation = []
        for i in range(len(operands)):
            permutation.append(operands[i])
            if i < len(combo):
                permutation.append(combo[i])
        equation = ''.join(permutation)
        result = eval(equation)
        if result == target:
            return True
    return False


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))
