import time
from collections import defaultdict
from utilities.coordinate import TurnDirection, Coordinate

def print_map(map):
    min_x = min(coord.x for coord in map.keys())
    max_x = max(coord.x for coord in map.keys())
    min_y = min(coord.y for coord in map.keys())
    max_y = max(coord.y for coord in map.keys())

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(map[Coordinate(x, y)], end='')
        print()

def main():
    with open("input/day6.txt", "r") as file:
        file_content = file.read().splitlines()

    guard, map = parse_map(file_content)
    guard_direction = Coordinate.South

    path = part_one(guard, guard_direction, map)
    result = len(set(path))
    result2 = part_two(guard, guard_direction, map, set(path))

    print(result)
    print(result2)

def part_two(guard, guard_direction, map, path):
    count = 0
    for coord in path:
        pixel = map[coord]
        if pixel == '.':
            result = find_loop(guard, guard_direction, map, coord)
            if result == 'loop':
                count += 1

    return count

def find_loop(guard, guard_direction, map, blocked_coord):
    visited = {(guard, guard_direction)}
    while True:
        next_position = guard + guard_direction
        next_pixel = map[next_position]

        if next_pixel == '0':
            return 'exit'
        elif next_pixel == '#' or next_position == blocked_coord:
            guard_direction = guard_direction.turn(TurnDirection.LEFT)
        else:
            if (next_position, guard_direction) in visited:
                return 'loop'
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
    map = defaultdict(lambda: '0')
    y = 0
    for line in file_content:
        x = 0
        for pixel in line:
            coord = Coordinate(x, y)
            map[coord] = pixel
            x += 1
        y += 1
    guard = next((coord for coord, val in map.items() if val == '^'), None)
    map[guard] = '.'
    return guard, map

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))
