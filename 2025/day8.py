import math
import time
from itertools import combinations



class Box:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.connections = set()
        self.circuit_id = None

    def distance_to(self, other: 'Box') -> float:
        return math.dist([self.x, self.y, self.z], [other.x, other.y, other.z])

    def __eq__(self, other):
        if not isinstance(other, Box):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def main():
    with open("input/day8.txt", "r") as file:
        file_content = file.read().splitlines()

    boxes = [Box(*map(int, box.split(','))) for box in file_content]

    circuits = {}
    for i in range(len(boxes)):
        circuits[i] = set([boxes[i]] + [])
        boxes[i].circuit_id = i

    possible_connections = []
    for b1, b2 in combinations(boxes, 2):
        if b1 != b2:
            possible_connections.append([b1, b2, b1.distance_to(b2), False])

    possible_connections.sort(key=lambda x: x[2])

    i = 0
    while True:
        closest_pair = next(pair for pair in possible_connections if not pair[3])
        closest_pair[0].connections.add(closest_pair[1])
        closest_pair[1].connections.add(closest_pair[0])
        closest_pair[3] = True

        id_to_merge = closest_pair[1].circuit_id
        id_to_merge_into = closest_pair[0].circuit_id
        if id_to_merge != id_to_merge_into:
            for connected_box in circuits[id_to_merge]:
                connected_box.circuit_id = id_to_merge_into
                circuits[id_to_merge_into].add(connected_box)
            del circuits[id_to_merge]
            print(f"i: {i}. Id {id_to_merge} merged into {id_to_merge_into}")
        if i == 1000:
            sorted_circuits = sorted(circuits.values(), key=len, reverse=True)
            biggest_circuits = [len(circuit) for circuit in sorted_circuits[:3]]

            print(math.prod(biggest_circuits))
            #break

        if len(circuits) == 1:
            print(closest_pair[0].x * closest_pair[1].x)
            break

        i += 1


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))