import itertools
import math
import time

from utilities.coordinate import extract_map, Coordinate


def main():
    with open("input/day7.txt", "r") as file:
        file_content = file.read().splitlines()

    grid = extract_map(file_content, '.')
    start = [key for key, value in grid.items() if value == 'S'][0]
    max_y = max(grid.keys(), key=lambda x: x.y).y

    splits = 0
    timelines = 0

    beams = {start: 1}

    while True:
        new_beams = {}
        step_splits = 0

        for beam, count in beams.items():
            next_coord = beam + Coordinate.North
            if next_coord not in grid:
                timelines += count
                continue

            val = grid[next_coord]
            if val == '.':
                new_beams[next_coord] = new_beams.get(next_coord, 0) + count
            elif val == '^':
                step_splits += 1
                east = next_coord + Coordinate.East
                west = next_coord + Coordinate.West
                new_beams[east] = new_beams.get(east, 0) + count
                new_beams[west] = new_beams.get(west, 0) + count

        if step_splits > 0:
            splits += step_splits

        beams = new_beams
        if not beams:
            break

    print(splits)
    print(timelines)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))