scoreVals = {
    "X": 1,
    "O": -1,
    "tie": 0
}


def bestMove(inputBoard):
    bestScore = float("-inf")
    for x in range(1, 10):
        if inputBoard.checkIfEmpty(x) == True:
            cordX, cordY = inputBoard.getCords(x)

            inputBoard.board[cordX, cordY] = "O"
            score = minimax(inputBoard, 0, True)
            inputBoard.board[cordX, cordY] = " "

            if score > bestScore:
                bestScore = score
                bestMove = [cordX, cordY]
    inputBoard.board[bestMove[0], bestMove[1]] = "O"


def minimax(inputBoard, depth, isMaximize):
    # if(isMaximize):

    return 1
