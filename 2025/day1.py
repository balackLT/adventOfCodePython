import time


def main():
    with open("input/day1.txt", "r") as file:
        file_content = file.read().splitlines()

    dial = 50
    count1 = 0
    count2 = 0

    for line in file_content:
        direction = line[0]
        distance = int(line[1:]) % 100
        count2 += int(line[1:]) // 100

        if direction == "R":
            dial += distance
        else:
            dial -= distance

        if dial == 0 or dial == 100:
            dial = 0
            count1 += 1
        elif dial > 99:
            if dial - distance != 0:
                count2 += 1
            dial -= 100
        elif dial < 0 :
            if dial + distance != 0:
                count2 += 1
            dial += 100

    print(count1)
    print(count1 + count2)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))