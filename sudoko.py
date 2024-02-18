#game is in process 
class SudokoBoard:
    def __init__(self,data):
        self.puzzleCellData = {
            (0, 0): -1, (0, 1): -1, (0, 2): -1, (0, 3): -1, (0, 4): -1, (0, 5): -1, (0, 6): -1, (0, 7): -1, (0, 8): -1,
            (1, 0): -1, (1, 1): -1, (1, 2): -1, (1, 3): -1, (1, 4): -1, (1, 5): -1, (1, 6): -1, (1, 7): -1, (1, 8): -1,
            (2, 0): -1, (2, 1): -1, (2, 2): -1, (2, 3): -1, (2, 4): -1, (2, 5): -1, (2, 6): -1, (2, 7): -1, (2, 8): -1,
            (3, 0): -1, (3, 1): -1, (3, 2): -1, (3, 3): -1, (3, 4): -1, (3, 5): -1, (3, 6): -1, (3, 7): -1, (3, 8): -1,
            (4, 0): -1, (4, 1): -1, (4, 2): -1, (4, 3): -1, (4, 4): -1, (4, 5): -1, (4, 6): -1, (4, 7): -1, (4, 8): -1,
            (5, 0): -1, (5, 1): -1, (5, 2): -1, (5, 3): -1, (5, 4): -1, (5, 5): -1, (5, 6): -1, (5, 7): -1, (5, 8): -1,
            (6, 0): -1, (6, 1): -1, (6, 2): -1, (6, 3): -1, (6, 4): -1, (6, 5): -1, (6, 6): -1, (6, 7): -1, (6, 8): -1,
            (7, 0): -1, (7, 1): -1, (7, 2): -1, (7, 3): -1, (7, 4): -1, (7, 5): -1, (7, 6): -1, (7, 7): -1, (7, 8): -1,
            (8, 0): -1, (8, 1): -1, (8, 2): -1, (8, 3): -1, (8, 4): -1, (8, 5): -1, (8, 6): -1, (8, 7): -1, (8, 8): -1

        }
        self.setup(data)


        block1 = [self.puzzleCellData[0, 0], self.puzzleCellData[0, 1], self.puzzleCellData[0, 2],
                  self.puzzleCellData[1, 0],
                  self.puzzleCellData[1, 1], self.puzzleCellData[1, 2],
                  self.puzzleCellData[2, 0], self.puzzleCellData[2, 1], self.puzzleCellData[2, 2]]

        block2 = [self.puzzleCellData[0, 3], self.puzzleCellData[0, 4], self.puzzleCellData[0, 5],
                  self.puzzleCellData[1, 3], self.puzzleCellData[1, 4],
                  self.puzzleCellData[1, 5], self.puzzleCellData[2, 3], self.puzzleCellData[2, 4],
                  self.puzzleCellData[2, 5]]

        block3 = [self.puzzleCellData[0, 6], self.puzzleCellData[0, 7], self.puzzleCellData[0, 8],
                  self.puzzleCellData[1, 6],
                  self.puzzleCellData[1, 7], self.puzzleCellData[1, 8],
                  self.puzzleCellData[2, 6], self.puzzleCellData[2, 7], self.puzzleCellData[2, 8]]

        block4 = [
            self.puzzleCellData[3, 0], self.puzzleCellData[3, 1], self.puzzleCellData[3, 2],
            self.puzzleCellData[4, 0], self.puzzleCellData[4, 1], self.puzzleCellData[4, 2],
            self.puzzleCellData[5, 0], self.puzzleCellData[5, 1], self.puzzleCellData[5, 2],

        ]
        block5 = [
            self.puzzleCellData[3, 3], self.puzzleCellData[3, 4], self.puzzleCellData[3, 5],
            self.puzzleCellData[4, 3], self.puzzleCellData[4, 4], self.puzzleCellData[4, 5],
            self.puzzleCellData[5, 3], self.puzzleCellData[5, 4], self.puzzleCellData[5, 5],
        ]

        block6 = [

            self.puzzleCellData[3, 6], self.puzzleCellData[3, 7], self.puzzleCellData[3, 8],
            self.puzzleCellData[4, 6], self.puzzleCellData[4, 6], self.puzzleCellData[4, 8],
            self.puzzleCellData[5, 6], self.puzzleCellData[5, 7], self.puzzleCellData[5, 8],
        ]

        block7 = [

            self.puzzleCellData[6, 0], self.puzzleCellData[6, 1], self.puzzleCellData[6, 2],
            self.puzzleCellData[7, 0], self.puzzleCellData[7, 1], self.puzzleCellData[7, 2],
            self.puzzleCellData[8, 0], self.puzzleCellData[8, 1], self.puzzleCellData[8, 2],
        ]
        block8 = [

            self.puzzleCellData[6, 3], self.puzzleCellData[3, 4], self.puzzleCellData[6, 5],
            self.puzzleCellData[7, 3], self.puzzleCellData[7, 4], self.puzzleCellData[7, 5],
            self.puzzleCellData[8, 3], self.puzzleCellData[8, 4], self.puzzleCellData[8, 5],
        ]
        block9 = [

            self.puzzleCellData[6, 6], self.puzzleCellData[3, 7], self.puzzleCellData[6, 8],
            self.puzzleCellData[7, 6], self.puzzleCellData[7, 7], self.puzzleCellData[7, 8],
            self.puzzleCellData[8, 6], self.puzzleCellData[8, 7], self.puzzleCellData[8, 8],
        ]

    def setup(self,data):
        for i in range(9):
            for j in range(9):
                value = data[i][j]
                if value != -1:
                    self.puzzleCellData[i,j] = value
    def display(self):
        row = 0
        column = 0

        for i in range(0, 9):

            for j in range(0, 9):
                prefix = " "
                value = "-" if self.puzzleCellData[(i, j)] == -1 else self.puzzleCellData[(i, j)]
                print(prefix + str(value) + " ", end="")

            print()
        return 0

    def IsInBlock(self,currentCell, option):
        pass

    def IsInColumn(self,currentCell, option):
        pass

    def IsInRow(self,currentCell, option):
        row,col = currentCell
        i = 0
        while row <= 8:
            if i != row and self.puzzleCellData[i,col] == option:
                return True
            else :
                i += 1


    def getNextCell(self,currentCell):
        pass

    def getPossibleOptions(self,currentCell):
        allNumbers = []
        for i in range(1, 10):
            if not (self.IsInRow(currentCell, i) and self.IsInBlock(currentCell, i) and self.IsInColumn(currentCell, i)):
                allNumbers.append(i)

        return allNumbers

    def gameOver(self):
        print("All Cells are filled up ")

    def findingPlace(self,PossibleOptions, currentCell):
        if not PossibleOptions:
            return

        for option in PossibleOptions:
            self.puzzleCellData[currentCell] = option

            self.findingPlace(self.getPossibleOptions(), self.getNextCell(currentCell))

            # removing
            self.puzzleCellData[currentCell] = -1

        return self.gameOver()


data = [
    [-1, 3, 9, -1, -1, -1, -1, -1, 2],
    [-1, -1, -1, -1, -1, -1, 8, 6, -1],
    [4, -1, -1, 5, 7, -1, 1, -1, -1],
    [-1, 9, -1, 1, -1, -1, -1, -1, -1],
    [-1, 2, -1, -1, -1, 6, 3, -1, 8],
    [6, -1, 8, 4, -1, 3, -1, 1, 5],

    [-1, -1, -1, 6, 3, 1, -1, 9, -1],
    [7, -1, 5, -1, -1, 8, -1, 2, -1],
    [-1, -1, -1, 2, -1, -1, 4, -1, -1]
]

board = SudokoBoard(data)
board.display()

