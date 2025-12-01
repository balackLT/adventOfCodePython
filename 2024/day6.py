import time
from enum import Enum, auto

from utilities.coordinate import TurnDirection, Coordinate, print_map, extract_map

class LoopResult(Enum):
    LOOP = auto()
    EXIT = auto()

def main():
    with open("input/day6.txt", "r") as file:
        file_content = file.read().splitlines()

    guard, map = parse_map(file_content)
    guard_direction = Coordinate.South

    path = part_one(guard, guard_direction, map)
    result = len(set(path))
    print(result)

    result2 = part_two(guard, guard_direction, map, set(path))
    print(result2)

def part_two(guard, guard_direction, map, path):
    count = 0
    for coord in path:
        result = find_loop(guard, guard_direction, map, coord)
        if result == LoopResult.LOOP:
            count += 1

    return count

def find_loop(guard, guard_direction, map, blocked_coord):
    visited = {(guard, guard_direction)}
    while True:
        next_position = guard + guard_direction
        next_pixel = map[next_position]

        if next_pixel == '0':
            return LoopResult.EXIT
        elif next_pixel == '#' or next_position == blocked_coord:
            guard_direction = guard_direction.turn(TurnDirection.LEFT)
        else:
            if (next_position, guard_direction) in visited:
                return LoopResult.LOOP
            guard = next_position
            visited.add((next_position, guard_direction))

def part_one(guard, guard_direction, map):
    visited = {guard}
    while True:
        next_position = guard + guard_direction
        next_pixel = map[next_position]

        if next_pixel == '0':
            break
        elif next_pixel == '#':
            guard_direction = guard_direction.turn(TurnDirection.LEFT)
        else:
            guard = next_position
            # map[next_position] = 'X'
            visited.add(next_position)
        # print_map(map)
        # print('')
    return visited

def parse_map(file_content):
    map = extract_map(file_content, '0')
    guard = next((coord for coord, val in map.items() if val == '^'), None)
    map[guard] = '.'
    return guard, map

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))
