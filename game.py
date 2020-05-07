from board import Board
from ai import bestMove

game_board = Board()


countinue = False
moves = 0
player_turn = True

while game_board.checkWin() == None and moves != 9:
    if player_turn:
        # X always go first, player is always X
        while countinue == False:
            countinue = game_board.insert(int(input("Location: ")), "X")
    else:
        while countinue == False:

            # UNCOMMENT IF TWOPLAYERS
            # countinue = game_board.insert(int(input("Location: ")), "O")

            # UNCOMMENT IF AI
            bestMove(game_board)
            countinue = True

    moves += 1
    player_turn = not player_turn
    countinue = False
    print(game_board)

print(game_board.checkWin() + " Wins!")
