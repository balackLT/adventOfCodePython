file = open("input/day1.txt", "r")
lines =  file.read().splitlines()

list1 = [int(line.split()[0]) for line in lines]
list2 = [int(line.split()[1]) for line in lines]

sorted1 = sorted(list1)
sorted2 = sorted(list2)

distance = 0
for i in range(len(sorted1)):
    dist = abs(sorted1[i] - sorted2[i])
    distance += dist

print(distance)

similarity = 0
for val in list1:
    sim1 = sum(x == val for x in list2) * val
    similarity += sim1

print(similarity)



