file = open("input/day4.txt", "r")
lines = file.read().splitlines()


class BingoNumber:
    def __init__(self, number):
        self.number = number
        self.marked = False

    def mark(self):
        self.marked = True

class BingoRow:
    def __init__(self):
        self.row = []

    def add(self, number):
        self.row.append(number)

class BingoBoard:
    def __init__(self):
        self.rows = []

    def add(self, bingo_row):
        self.rows.append(bingo_row)


bingo_numbers = lines[0].split(',')
boards = []
board = BingoBoard()
for line in lines[2:]:
    if len(line) == 0:
        boards.append(board)
        board = BingoBoard()
    else:
        row = BingoRow()
        for num in line.split():
            bingo_num = BingoNumber(num)
            row.add(bingo_num)
        board.add(row)

for bingo_number in bingo_numbers:
    for board in boards:
        for row in board.rows:
            for num in row.row:
                if num == bingo_number:
                    num.mark()

x = 0