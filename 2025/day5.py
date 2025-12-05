import itertools
import time


def is_fresh(ingredient, ranges):
    for low, high in ranges:
        if low <= ingredient <= high:
            return True
    return False

def overlaps(low1, high1, low2, high2):
    return low1 <= high2 and high1 >= low2


def merge_ranges(ranges):
    prev_ranges = ranges
    while True:
        merged_ranges = set()

        for low, high in prev_ranges:
            overlapping_ranges = [[l, h] for l, h in prev_ranges if overlaps(l, h, low, high)]
            #print(low, high, overlapping_ranges)
            merged_ranges.add((min(low, *map(lambda x: x[0], overlapping_ranges)), max(high, *map(lambda x: x[1], overlapping_ranges))))
            #print(merged_ranges)

        if merged_ranges == prev_ranges:
            break
        prev_ranges = merged_ranges

    return merged_ranges


def main():
    with open("input/day5.txt", "r") as file:
        file_content = file.read().splitlines()

    split = [list(y) for x, y in itertools.groupby(file_content, lambda z: z == '') if not x]
    ranges = [[int(num) for num in rng.split('-')] for rng in split[0]]
    ranges.sort(key=lambda x: x[0])
    ingredients = [int(num) for num in split[1]]

    ranges = merge_ranges(ranges)
    print(ranges)

    count = 0

    for ingredient in ingredients:
        count += is_fresh(ingredient, ranges)

    print(count)

    count2 = 0
    for low, high in ranges:
        count2 += (high - low + 1)

    print(count2)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))