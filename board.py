import numpy as np


class Board:
    def __init__(self):
        self.board = np.empty([3, 3], "str")
        self.board[:] = " "
        self.win_state = False

        # test
        init = 0
        for x in range(0, 3):
            for y in range(0, 3):
                self.board[x, y] = init
                init += 1

    def __str__(self):
        string = ""
        for x in range(0, 3):
            for y in range(0, 3):
                string += str(self.board[x, y]) + "|"
            string += '\n'
        return string

    def checkWin(self):
        # Check right Diag
        if (self.board[0, 0] == self.board[1, 1] == self.board[2, 2]) and (self.board[0, 0] == "X" or self.board[0, 0] == "O"):
            print("Diag")
            return True
        # Check left Diag
        elif (self.board[2, 0] == self.board[1, 1] == self.board[0, 2]) and (self.board[2, 0] == "X" or self.board[0, 0] == "O"):
            print("Diag")
            return True
        else:
            for x in range(0, 3):
                # check Rows
                if (self.board[x, 0] == self.board[x, 1] == self.board[x, 2]) and (self.board[x, 0] == "X" or self.board[x, 0] == "O"):
                    print("Row")
                    return True
                # Check Cols
                elif (self.board[0, x] == self.board[1, x] == self.board[2, x]) and (self.board[0, x] == "X" or self.board[0, x] == "O"):
                    print("Cols")
                    return True
                # Tie
                else:
                    return "No Winner"
