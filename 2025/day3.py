import time


def calculate_max_joltage(line: str, limit: int) -> int:
    split = [int(num) for num in line]
    nums = [0] * limit

    last_index = -1
    for j in range(limit):
        for i in range(last_index + 1, len(split) - (limit - j) + 1):
            current_num = split[i]
            if current_num > nums[j]:
                nums[j] = current_num
                last_index = i

    result = str.join("", [str(symbol) for symbol in nums])
    return int(result)


def main():
    with open("input/day3.txt", "r") as file:
        file_content = file.read().splitlines()

    maximum_joltage = 0

    for line in file_content:
        maximum_joltage += calculate_max_joltage(line, 2)

    print(maximum_joltage)

    maximum_joltage2 = 0

    for line in file_content:
        maximum_joltage2 += calculate_max_joltage(line, 12)

    print(maximum_joltage2)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))