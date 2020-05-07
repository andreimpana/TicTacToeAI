import numpy as np

# Dictionary for converting all numericals to cordinates
cordsDictionary = {
    1: "0,0",
    2: "0,1",
    3: "0,2",
    4: "1,0",
    5: "1,1",
    6: "1,2",
    7: "2,0",
    8: "2,1",
    9: "2,2"
}


class Board:

    def __init__(self):
        self.board = np.empty([3, 3], "str")
        self.board[:] = " "
        self.win_state = False

        # Prints board layout
        init = 1
        for x in range(0, 3):
            for y in range(0, 3):
                self.board[x, y] = init
                init += 1
        print(self)

        # Clears board
        self.board[:] = " "

    # Pretty print for the board
    def __str__(self):
        string = ""
        for x in range(0, 3):
            for y in range(0, 3):
                string += str(self.board[x, y]) + "|"
            string += '\n'
        return string

    def checkWin(self):
        # Check right Diag
        winner = None
        if (self.board[0, 0] == self.board[1, 1] == self.board[2, 2]) and (self.board[0, 0] == "X" or self.board[0, 0] == "O"):
            if(self.board[0, 0] == "X"):
                winner = "X"
            else:
                winner = "O"
        # Check left Diag
        elif (self.board[2, 0] == self.board[1, 1] == self.board[0, 2]) and (self.board[2, 0] == "X" or self.board[2, 0] == "O"):
            if(self.board[2, 0] == "X"):
                winner = "X"
            else:
                winner = "O"
        else:
            for x in range(0, 3):
                # Check Rows
                if (self.board[x, 0] == self.board[x, 1] == self.board[x, 2]) and (self.board[x, 0] == "X" or self.board[x, 0] == "O"):
                    # print("Row")
                    if(self.board[x, 0] == "X"):
                        winner = "X"
                    else:
                        winner = "O"
                # Check Cols
                elif (self.board[0, x] == self.board[1, x] == self.board[2, x]) and (self.board[0, x] == "X" or self.board[0, x] == "O"):
                    # print("Cols")
                    if(self.board[0, x] == "X"):
                        winner = "X"
                    else:
                        winner = "O"

        # Checks for tie
        openSpots = 0
        for x in range(0, 3):
            for y in range(0, 3):
                if self.board[x, y] == " ":
                    openSpots += 1

        if winner == None and openSpots == 0:
            winner = "tie"

        return winner

    # Inserts input into board
    def insert(self, location, player):
        cordX, cordY = self.getCords(location)
        if self.checkIfEmpty(location) == False:
            print("Spot taken, try again")
            return False
        else:
            self.board[cordX, cordY] = player
            return True

    # Converts int location of matrix into cordinates
    def getCords(self, x):
        cords = cordsDictionary[x]
        cords.split(",")
        return int(cords[0]), int(cords[2])

    # Checks if location in board is taken
    def checkIfEmpty(self, x):
        cordX, cordY = self.getCords(x)
        return self.board[cordX, cordY] == " "
