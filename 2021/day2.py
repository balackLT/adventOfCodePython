from coordinate import Coordinate

file = open("input/day2.txt", "r")
lines = file.read().splitlines()

position = Coordinate(0, 0)

for instruction in lines:
    split = instruction.split()
    match split[0]:
        case "up":
            position.y -= int(split[1])
        case "down":
            position.y += int(split[1])
        case "forward":
            position.x += int(split[1])

print(position.x * position.y)


position = Coordinate(0, 0)
aim = 0

for instruction in lines:
    split = instruction.split()
    match split[0]:
        case "up":
            aim -= int(split[1])
        case "down":
            aim += int(split[1])
        case "forward":
            position.x += int(split[1])
            position.y += int(split[1]) * aim

print(position.x * position.y)