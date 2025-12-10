import time
from collections import defaultdict
from itertools import combinations


from utilities.coordinate import Coordinate, print_map


def main():
    with open("input/day9.txt", "r") as file:
        file_content = file.read().splitlines()

    coordinates = [Coordinate.from_string(line) for line in file_content]

    rectangles = []
    for c1, c2 in combinations(coordinates, 2):
        if c1 != c2:
            rectangles.append((c1, c2, (abs(c1.x - c2.x) + 1) * (abs(c1.y - c2.y) + 1)))

    rectangles.sort(key=lambda x: x[2], reverse=True)
    print(rectangles[0][2])

    tiles = defaultdict(lambda: '.')
    previous_coordinate = coordinates[0]
    for coordinate in coordinates[1:]:
        between = previous_coordinate.coordinates_straight_between(coordinate)
        for coord in between:
            tiles[coord] = '#'
        previous_coordinate = coordinate

    between = previous_coordinate.coordinates_straight_between(coordinates[0])
    for coord in between:
        tiles[coord] = '#'

    print_map(tiles)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))