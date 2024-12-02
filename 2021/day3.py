file = open("input/day3.txt", "r")
lines = file.read().splitlines()

def gamma_count(list):
    gamma_counter = [0] * len(list[0])
    for line in list:
        for j in range(len(line)):
            gamma_counter[j] += int(line[j])
    gamma_bytes = []
    epsilon_bytes = []
    for value in gamma_counter:
        if value >= len(lines) / 2:
            gamma_bytes.append("1")
            epsilon_bytes.append("0")
        if value < len(lines) / 2:
            gamma_bytes.append("0")
            epsilon_bytes.append("1")

    gamma = int(''.join(gamma_bytes), 2)
    epsilon = int(''.join(epsilon_bytes), 2)
    return gamma_bytes, epsilon_bytes, gamma, epsilon

result = gamma_count(lines)

print(result[2] * result[3])


# part2
oxygen_list = lines.copy()
co2_list = lines.copy()

for i in range(len(lines[0])):
    counts = gamma_count(oxygen_list)
    gamma_byte = counts[0]
    oxygen_list = [x for x in oxygen_list if x[i] == gamma_byte[i]]

    if len(oxygen_list) == 1:
        break

for i in range(len(lines[0])):
    counts = gamma_count(co2_list)
    epsilon_byte = counts[1]
    co2_list = [x for x in co2_list if x[i] == epsilon_byte[i]]
    if len(co2_list) == 1:
        break

oxygen = int(oxygen_list[0], 2)
co2 = int(co2_list[0], 2)

print(oxygen * co2)
