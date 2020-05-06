from board import Board

game_board = Board()


countinue = False
moves = 0
player = False

while game_board.checkWin() == "No Winner" and moves != 9:
    if player == False:
        while countinue == False:
            countinue = game_board.insert(int(input("Location: ")), "X")
    else:
        while countinue == False:
            countinue = game_board.insert(int(input("Location: ")), "O")

    moves += 1
    player = not player
    countinue = False
    print(game_board)

if game_board.checkWin() == "No Winner" and moves == 9:
    print(game_board.checkWin())

# 514628379
