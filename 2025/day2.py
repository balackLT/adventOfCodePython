import time


def main():
    with open("input/day2.txt", "r") as file:
        file_content = file.read()

    pairs = [pair.split('-') for pair in file_content.split(',')]

    count1 = 0
    for pair in pairs:
        for num in range(int(pair[0]), int(pair[1])+1):
            length = len(str(num))
            if length % 2 == 0:
                half = length // 2
                first_half = str(num)[:half]
                second_half = str(num)[half:]
                if first_half == second_half:
                    count1 += num

    print(count1)

    count2 = 0
    for pair in pairs:
        for num in range(int(pair[0]), int(pair[1]) + 1):
            if check_number(num):
                count2 += num

    print(count2)


def check_number(num: int) -> bool:
    for repetition_length in range(1, len(str(num)) // 2 + 1):
        repeated_num = str(num)[:repetition_length] * (len(str(num)) // repetition_length)
        if repeated_num == str(num):
            return True
    return False

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))