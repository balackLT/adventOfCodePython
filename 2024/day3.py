import re

file = open("input/day3.txt", "r").read()

instructions = re.findall('mul\((\d+,\d+)\)', file)

result = 0
for instruction in instructions:
    result += int(instruction.split(',')[0]) * int(instruction.split(',')[1])

print(result)

instructions = re.findall('mul\((\d+,\d+)\)|(do)\(\)|(don\'t)\(\)', file)

result = 0
enabled = True
for instruction in instructions:
    if instruction[1] == 'do':
        enabled = True
    elif instruction[2] == 'don\'t':
        enabled = False
    elif enabled:
        result += int(instruction[0].split(',')[0]) * int(instruction[0].split(',')[1])

print(result)