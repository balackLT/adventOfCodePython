import itertools
import math
import time


def main():
    with open("input/day6.txt", "r") as file:
        file_content = file.read().splitlines()

    symbols = file_content[-1].split()
    numbers = [[int(num) for num in line.split()] for line in file_content[:-1]]

    count = 0
    columns = []
    for i in range(len(symbols)):
        nums = []
        for j in range(len(numbers)):
            nums.append(numbers[j][i])
        columns.append(nums)
        if symbols[i] == '+':
            count += sum(nums)
        elif symbols[i] == '*':
            count += math.prod(nums)

    print(count)
            
    line_columns = []
    longest_line = len(max(file_content[:-1], key=lambda x: len(x)))

    for i in range(longest_line, -1, -1):
        column = []
        for line in file_content[:-1]:

            if i >= len(line):
                symbol = ''
            else:
                symbol = line[i]
            column.append(symbol)
        line_columns.append(column)

    line_columns.pop(0)
    symbol_num = 1
    count2 = 0
    nums = []
    for column in line_columns:
        num_str = ''.join(symbol for symbol in column if symbol)
        if num_str.isspace() or num_str == '':
            num = -1
        else:
            num = int(num_str)
            nums.append(num)

        if num == -1:
            sym = symbols[-symbol_num]
            if sym == '+':
                count2 += sum(nums)
            elif sym == '*':
                count2 += math.prod(nums)
            symbol_num += 1
            nums = []
    sym = symbols[-symbol_num]
    if sym == '+':
        count2 += sum(nums)
    elif sym == '*':
        count2 += math.prod(nums)

    print(count2)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))