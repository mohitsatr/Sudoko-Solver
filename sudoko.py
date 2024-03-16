# game is in process
from puzzles import hard_1, hard_1_test_1,master_1


def gameOver():
    print("All Cells are filled up ")


class SudokoBoard:
    EMPTY = 0

    def __init__(self, data):

        self.puzzleCellData = {
            (0, 0): self.EMPTY, (0, 1): self.EMPTY, (0, 2): self.EMPTY, (0, 3): self.EMPTY, (0, 4): self.EMPTY,
            (0, 5): self.EMPTY, (0, 6): self.EMPTY, (0, 7): self.EMPTY, (0, 8): self.EMPTY,
            (1, 0): self.EMPTY, (1, 1): self.EMPTY, (1, 2): self.EMPTY, (1, 3): self.EMPTY, (1, 4): self.EMPTY,
            (1, 5): self.EMPTY, (1, 6): self.EMPTY, (1, 7): self.EMPTY, (1, 8): self.EMPTY,
            (2, 0): self.EMPTY, (2, 1): self.EMPTY, (2, 2): self.EMPTY, (2, 3): self.EMPTY, (2, 4): self.EMPTY,
            (2, 5): self.EMPTY, (2, 6): self.EMPTY, (2, 7): self.EMPTY, (2, 8): self.EMPTY,
            (3, 0): self.EMPTY, (3, 1): self.EMPTY, (3, 2): self.EMPTY, (3, 3): self.EMPTY, (3, 4): self.EMPTY,
            (3, 5): self.EMPTY, (3, 6): self.EMPTY, (3, 7): self.EMPTY, (3, 8): self.EMPTY,
            (4, 0): self.EMPTY, (4, 1): self.EMPTY, (4, 2): self.EMPTY, (4, 3): self.EMPTY, (4, 4): self.EMPTY,
            (4, 5): self.EMPTY, (4, 6): self.EMPTY, (4, 7): self.EMPTY, (4, 8): self.EMPTY,
            (5, 0): self.EMPTY, (5, 1): self.EMPTY, (5, 2): self.EMPTY, (5, 3): self.EMPTY, (5, 4): self.EMPTY,
            (5, 5): self.EMPTY, (5, 6): self.EMPTY, (5, 7): self.EMPTY, (5, 8): self.EMPTY,
            (6, 0): self.EMPTY, (6, 1): self.EMPTY, (6, 2): self.EMPTY, (6, 3): self.EMPTY, (6, 4): self.EMPTY,
            (6, 5): self.EMPTY, (6, 6): self.EMPTY, (6, 7): self.EMPTY, (6, 8): self.EMPTY,
            (7, 0): self.EMPTY, (7, 1): self.EMPTY, (7, 2): self.EMPTY, (7, 3): self.EMPTY, (7, 4): self.EMPTY,
            (7, 5): self.EMPTY, (7, 6): self.EMPTY, (7, 7): self.EMPTY, (7, 8): self.EMPTY,
            (8, 0): self.EMPTY, (8, 1): self.EMPTY, (8, 2): self.EMPTY, (8, 3): self.EMPTY, (8, 4): self.EMPTY,
            (8, 5): self.EMPTY, (8, 6): self.EMPTY, (8, 7): self.EMPTY, (8, 8): self.EMPTY

        }
        self.setup(data)

        self.BoardFilled = False
        self.block1 = [[0, 0], [0, 1], [0, 2],
                       [1, 0], [1, 1], [1, 2],
                       [2, 0], [2, 1], [2, 2]]

        self.block2 = [[0, 3], [0, 4], [0, 5],
                       [1, 3], [1, 4], [1, 5],
                       [2, 3], [2, 4], [2, 5]]

        self.block3 = [[0, 6], [0, 7], [0, 8],
                       [1, 6], [1, 7], [1, 8],
                       [2, 6], [2, 7], [2, 8]]

        self.block4 = [
            [3, 0], [3, 1], [3, 2],
            [4, 0], [4, 1], [4, 2],
            [5, 0], [5, 1], [5, 2],

        ]
        self.block5 = [
            [3, 3], [3, 4], [3, 5],
            [4, 3], [4, 5],
            [5, 3], [5, 5],
        ]

        self.block6 = [

            [3, 6], [3, 7], [3, 8],
            [4, 6], [4, 6], [4, 8],
            [5, 6], [5, 7], [5, 8],
        ]

        self.block7 = [

            [6, 0], [6, 1], [6, 2],
            [7, 0], [7, 1], [7, 2],
            [8, 0], [8, 1], [8, 2],
        ]
        self.block8 = [

            [6, 3], [6, 4], [6, 5],
            [7, 3], [7, 4], [7, 5],
            [8, 3], [8, 4], [8, 5],
        ]
        self.block9 = [

            [6, 6], [6, 7], [6, 8],
            [7, 6], [7, 7], [7, 8],
            [8, 6], [8, 7], [8, 8],
        ]

    def setup(self, data):
        for i in range(9):
            for j in range(9):
                value = data[i][j]
                if value != self.EMPTY:
                    self.puzzleCellData[i, j] = value

    def display(self):
        print(
            f"{self.puzzleCellData[0, 0]} {self.puzzleCellData[0, 1]} {self.puzzleCellData[0, 2]} | {self.puzzleCellData[0, 3]} {self.puzzleCellData[0, 4]} {self.puzzleCellData[0, 5]} | {self.puzzleCellData[0, 6]} {self.puzzleCellData[0, 7]} {self.puzzleCellData[0, 8]}")

        print(
            f"{self.puzzleCellData[1, 0]} {self.puzzleCellData[1, 1]} {self.puzzleCellData[1, 2]} | {self.puzzleCellData[1, 3]} {self.puzzleCellData[1, 4]} {self.puzzleCellData[1, 5]} | {self.puzzleCellData[1, 6]} {self.puzzleCellData[1, 7]} {self.puzzleCellData[1, 8]}")

        print(
            f"{self.puzzleCellData[2, 0]} {self.puzzleCellData[2, 1]} {self.puzzleCellData[2, 2]} | {self.puzzleCellData[2, 3]} {self.puzzleCellData[2, 4]} {self.puzzleCellData[2, 5]} | {self.puzzleCellData[2, 6]} {self.puzzleCellData[2, 7]} {self.puzzleCellData[2, 8]}")

        print("-  -  +  -  - +  -  -")
        print(
            f"{self.puzzleCellData[3, 0]} {self.puzzleCellData[3, 1]} {self.puzzleCellData[3, 2]} | {self.puzzleCellData[3, 3]} {self.puzzleCellData[3, 4]} {self.puzzleCellData[3, 5]} | {self.puzzleCellData[3, 6]} {self.puzzleCellData[3, 7]} {self.puzzleCellData[3, 8]}")

        print(
            f"{self.puzzleCellData[4, 0]} {self.puzzleCellData[4, 1]} {self.puzzleCellData[4, 2]} | {self.puzzleCellData[4, 3]} {self.puzzleCellData[4, 4]} {self.puzzleCellData[4, 5]} | {self.puzzleCellData[4, 6]} {self.puzzleCellData[4, 7]} {self.puzzleCellData[4, 8]}")

        print(
            f"{self.puzzleCellData[5, 0]} {self.puzzleCellData[5, 1]} {self.puzzleCellData[5, 2]} | {self.puzzleCellData[5, 3]} {self.puzzleCellData[5, 4]} {self.puzzleCellData[5, 5]} | {self.puzzleCellData[5, 6]} {self.puzzleCellData[5, 7]} {self.puzzleCellData[5, 8]}")
        print("-  -  +  -  - +  -  -")
        print(
            f"{self.puzzleCellData[6, 0]} {self.puzzleCellData[6, 1]} {self.puzzleCellData[6, 2]} | {self.puzzleCellData[6, 3]} {self.puzzleCellData[6, 4]} {self.puzzleCellData[6, 5]} | {self.puzzleCellData[6, 6]} {self.puzzleCellData[6, 7]} {self.puzzleCellData[6, 8]}")

        print(
            f"{self.puzzleCellData[7, 0]} {self.puzzleCellData[7, 1]} {self.puzzleCellData[7, 2]} | {self.puzzleCellData[7, 3]} {self.puzzleCellData[7, 4]} {self.puzzleCellData[7, 5]} | {self.puzzleCellData[7, 6]} {self.puzzleCellData[7, 7]} {self.puzzleCellData[7, 8]}")

        print(
            f"{self.puzzleCellData[8, 0]} {self.puzzleCellData[8, 1]} {self.puzzleCellData[8, 2]} | {self.puzzleCellData[8, 3]} {self.puzzleCellData[8, 4]} {self.puzzleCellData[8, 5]} | {self.puzzleCellData[8, 6]} {self.puzzleCellData[8, 7]} {self.puzzleCellData[8, 8]}")

    def look_up(self):
        pass

    def IsInBlock(self, currentCell, option):

        if list(currentCell) in self.block1:
            for cell in self.block1:
                if cell != list(currentCell) and self.puzzleCellData[tuple(cell)] == option:
                    return True
        elif list(currentCell) in self.block2:
            for cell in self.block2:
                if cell != list(currentCell) and self.puzzleCellData[tuple(cell)] == option:
                    return True

        elif list(currentCell) in self.block3:
            for cell in self.block3:
                if cell != list(currentCell) and self.puzzleCellData[tuple(cell)] == option:
                    return True

        elif list(currentCell) in self.block4:
            for cell in self.block4:
                if cell != list(currentCell) and self.puzzleCellData[tuple(cell)] == option:
                    return True


        elif list(currentCell) in self.block5:
            for cell in self.block5:
                if cell != list(currentCell) and self.puzzleCellData[tuple(cell)] == option:
                    return True


        elif list(currentCell) in self.block6:
            for cell in self.block6:
                if cell != list(currentCell) and self.puzzleCellData[tuple(cell)] == option:
                    return True

        elif list(currentCell) in self.block7:
            for cell in self.block7:
                if cell != list(currentCell) and self.puzzleCellData[tuple(cell)] == option:
                    return True

        elif list(currentCell) in self.block8:
            for cell in self.block8:
                if cell != list(currentCell) and self.puzzleCellData[tuple(cell)] == option:
                    return True


        elif list(currentCell) in self.block9:
            for cell in self.block9:
                if cell != list(currentCell) and self.puzzleCellData[tuple(cell)] == option:
                    return True
        return False

    def IsInColumn(self, currentCell, option):

        row, col = currentCell
        i = 0
        while i < 9:
            if i != col and self.puzzleCellData[row, i] == option:
                return True
            else:
                i += 1

        return False

    def IsInRow(self, currentCell, option):
        row, col = currentCell
        i = 0
        while i < 9:
            if i != row and self.puzzleCellData[i, col] == option:
                return True
            else:
                i += 1

        return False

    def getNextCell(self, currentCell):
        row, col = currentCell

        if row == 8 and col == 8:
            self.BoardFilled = True
            return self.EMPTY

        increment = 1
        while self.puzzleCellData[row, col] != self.EMPTY:
            if col == 8:
                row += 1
                col = 0

            else:
                col += increment

        return (row, col)


def getPossibleOptions(board, currentCell):
    allNumbers = []
    for i in range(1, 10):
        if not board.IsInBlock(currentCell, i):
            if board.IsInRow(currentCell, i) == False and board.IsInColumn(currentCell, i) == False:
                allNumbers.append(i)

    return allNumbers


def findingPlace(board, PossibleOptions, currentCell):
    if not PossibleOptions:
        print("NO possible Options for " + str(currentCell))
        return

    for option in PossibleOptions:
        print("filling " + str(currentCell) + " with " + str(option) + " from " + str(PossibleOptions))
        board.puzzleCellData[currentCell] = option

        board.display()
        print()

        nextCell = board.getNextCell(currentCell)
        if nextCell != board.EMPTY:
            findingPlace(board, getPossibleOptions(board, nextCell), nextCell)

            if not board.BoardFilled:
                # removing
                print("Removing " + str(currentCell))
                board.puzzleCellData[currentCell] = board.EMPTY

            else:
                break

        else:
            print("Game is Over")


data = [
    [0, 3, 9, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 8, 6, 0],
    [4, 0, 0, 5, 7, 0, 1, 0, 0],

    [0, 9, 0, 1, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 6, 3, 0, 8],
    [6, 0, 8, 4, 0, 3, 0, 1, 5],

    [0, 0, 0, 6, 3, 1, 0, 9, 0],
    [7, 0, 5, 0, 0, 8, 0, 2, 0],
    [0, 0, 0, 2, 0, 0, 4, 0, 0]
]

first_6_rows_filled = [
    [1, 3, 9, 8, 6, 4, 7, 5, 2],
    [2, 5, 7, 3, 1, 9, 8, 6, 4],
    [4, 8, 6, 5, 7, 2, 1, 3, 9],

    [3, 9, 4, 1, 8, 5, 2, 7, 6],
    [5, 2, 1, 7, 9, 6, 3, 4, 8],
    [6, 7, 8, 4, 2, 3, 9, 1, 5],

    # [0, 0, 0, 6, 3, 1, 0, 9, 0],
    [8, 4, 2, 6, 3, 1, 5, 9, 0],
    [7, 0, 5, 0, 0, 8, 0, 2, 0],
    [0, 0, 0, 2, 0, 0, 4, 0, 0]
]
fresh_board = SudokoBoard(master_1)
test_board = SudokoBoard(master_1)
findingPlace(fresh_board, getPossibleOptions(fresh_board, (0, 0)), (0, 0))
print(getPossibleOptions(test_board, (0, 0)))
