import time

from utilities.coordinate import extract_map


def main():
    with open("input/day4.txt", "r") as file:
        file_content = file.read().splitlines()

    grid = extract_map(file_content, '.')

    count = 0
    for item in [k for k, v in grid.items() if v == '@']:
        surrounding = item.get_adjacent_with_diagonals()
        rolls = 0
        for coord in surrounding:
            if grid[coord] == '@':
                rolls += 1
        if rolls < 4:
            count += 1

    print(count)

    removed = 0
    while True:
        to_remove = []
        for item in [k for k, v in grid.items() if v == '@']:
            surrounding = item.get_adjacent_with_diagonals()
            rolls = 0
            for coord in surrounding:
                if grid[coord] == '@':
                    rolls += 1
            if rolls < 4:
                to_remove.append(item)

        if len(to_remove) == 0:
            break
        for item in to_remove:
            removed += 1
            del grid[item]

    print(removed)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))