import time
from typing import List, Tuple


def parse_machine(line: str) -> Tuple[int, List[List[int]], List[int]]:
    split = line.split()
    diagram_string = split[0].strip("[]")
    diagram = 0
    for i, char in enumerate(diagram_string):
        if char == "#":
            diagram |= (1 << i)

    buttons = []
    for button in split[1:-1]:
        stripped = button.strip("()")
        nums = [int(num) for num in stripped.split(",")]
        buttons.append(nums)

    joltage_target = [int(num) for num in split[-1].strip("{}").split(',')]

    return diagram, buttons, joltage_target


def solve(target: int, buttons: List[List[int]]) -> int:
    start = 0

    steps = 0
    states = set()
    states.add(start)
    while True:
        steps += 1
        new_states = set()
        for state in states:
            for button in buttons:
                new_state = state
                for bit in button:
                    new_state ^= (1 << bit)
                if new_state == target:
                    return steps
                new_states.add(new_state)
        states = new_states


def multiply(polynomial: List[int], buttons: List[List[int]]):
    pass


def solve_joltage(target: List[int], buttons: List[List[int]]) -> int:
    polynomial = tuple([0 for _ in range(len(target))])

    result = multiply(polynomial, buttons)

    return 0


def main():
    with open("input/day10.txt", "r") as file:
        file_content = file.read().splitlines()

    machines = []
    for line in file_content:
        machines.append(parse_machine(line))

    # print(machines)

    count = 0

    i = 0
    for machine in machines:
        count += solve(machine[0], machine[1])

    print(count)

    count = 0
    for machine in machines:
        count += solve_joltage(machine[2], machine[1])
        print(i)
        i += 1

    print(count)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))