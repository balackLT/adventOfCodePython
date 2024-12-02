import math

file = open("input/day1.txt", "r")
lines =  [int(item) for item in file.read().splitlines()]

increased = 0
previous = math.inf

for depths in lines:
    if depths > previous:
        increased += 1
    
    previous = depths

print(increased)