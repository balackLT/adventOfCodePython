from collections import defaultdict
from typing import Iterable, List
from math import atan2, pi
from enum import Enum, auto

class TurnDirection(Enum):
    LEFT = auto()
    RIGHT = auto()

class Coordinate:
    Zero = None
    North = None
    South = None
    East = None
    West = None
    Down = None
    Up = None
    Right = None
    Left = None
    NorthWest = None
    NorthEast = None
    SouthWest = None
    SouthEast = None

    Directions = []
    ExtendedDirections = []

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def init_static(cls):
        cls.Zero = cls(0, 0)
        cls.North = cls(0, 1)
        cls.South = cls(0, -1)
        cls.East = cls(1, 0)
        cls.West = cls(-1, 0)
        cls.Down = cls(0, 1)
        cls.Up = cls(0, -1)
        cls.Right = cls(1, 0)
        cls.Left = cls(-1, 0)
        cls.NorthWest = cls(-1, 1)
        cls.NorthEast = cls(1, 1)
        cls.SouthWest = cls(-1, -1)
        cls.SouthEast = cls(1, -1)

        cls.Directions = [cls.North, cls.South, cls.West, cls.East]
        cls.ExtendedDirections = [cls.North, cls.South, cls.West, cls.East, cls.NorthEast, cls.NorthWest, cls.SouthEast, cls.SouthWest]

    @classmethod
    def from_string(cls, input_str: str, separator: str = ',') -> 'Coordinate':
        parts = input_str.split(separator)
        return cls(int(parts[0]), int(parts[1]))

    def turn(self, turn_direction: TurnDirection) -> 'Coordinate':
        if turn_direction == TurnDirection.LEFT:
            return Coordinate(self.y * -1, self.x)
        elif turn_direction == TurnDirection.RIGHT:
            return Coordinate(self.y, self.x * -1)

    def coordinates_straight_between(self, target: 'Coordinate') -> Iterable['Coordinate']:
        current = self
        while current != target:
            yield current
            current = current.move_towards(target)
        yield current

    def move_towards(self, coordinate: 'Coordinate') -> 'Coordinate':
        return min(self.get_adjacent_with_diagonals(), key=lambda c: c.manhattan_distance(coordinate))

    def get_adjacent_with_diagonals(self) -> List['Coordinate']:
        return [
            self + Coordinate.North,
            self + Coordinate.South,
            self + Coordinate.West,
            self + Coordinate.East,
            self + Coordinate.North + Coordinate.West,
            self + Coordinate.North + Coordinate.East,
            self + Coordinate.South + Coordinate.West,
            self + Coordinate.South + Coordinate.East
        ]

    def manhattan_distance(self, other: 'Coordinate' = None) -> int:
        if other is None:
            other = Coordinate.Zero
        return abs(self.x - other.x) + abs(self.y - other.y)

    def coordinates_within_distance(self, distance: int) -> Iterable['Coordinate']:
        for x in range(self.x - distance, self.x + distance + 1):
            for y in range(self.y - distance, self.y + distance + 1):
                if abs(self.x - x) + abs(self.y - y) <= distance:
                    yield Coordinate(x, y)

    def angle_between(self, target: 'Coordinate') -> float:
        radians = atan2(target.y - self.y, target.x - self.x)
        return (180 / pi) * radians

    def normalize(self) -> 'Coordinate':
        if self.x > 0:
            return Coordinate(1, 0)
        if self.x < 0:
            return Coordinate(-1, 0)
        if self.y > 0:
            return Coordinate(0, 1)
        if self.y < 0:
            return Coordinate(0, -1)
        return Coordinate(0, 0)

    def __eq__(self, other: 'Coordinate') -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Coordinate') -> 'Coordinate':
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Coordinate') -> 'Coordinate':
        return Coordinate(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> 'Coordinate':
        return Coordinate(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> 'Coordinate':
        return self.__mul__(other)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

# Initialize static members
Coordinate.init_static()

def print_map(coordinate_map: dict[Coordinate, str]):
    min_x = min(coord.x for coord in coordinate_map.keys())
    max_x = max(coord.x for coord in coordinate_map.keys())
    min_y = min(coord.y for coord in coordinate_map.keys())
    max_y = max(coord.y for coord in coordinate_map.keys())

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(coordinate_map[Coordinate(x, y)], end='')
        print()

def extract_map(file_content: list[str], default_char: str) -> dict[Coordinate, str]:
    coordinate_map = defaultdict(lambda: default_char)
    y = 0
    for line in file_content:
        x = 0
        for pixel in line:
            coord = Coordinate(x, y)
            coordinate_map[coord] = pixel
            x += 1
        y += 1
    return coordinate_map