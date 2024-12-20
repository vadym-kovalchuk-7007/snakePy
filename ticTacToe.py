from functools import reduce

defValue = " "
turnX = "X"
turnO = "O"
topL = "top-L"
topM = "top-M"
topR = "top-R"
midL = "mid-L"
midM = "mid-M"
midR = "mid-R"
lowL = "low-L"
lowM = "low-M"
lowR = "low-R"


def buildEmptyBoard(board: dict) -> dict:
    for key in [topL, topM, topR, midL, midM, midR, lowL, lowM, lowR]:
        board.setdefault(key, defValue)
    return board


board = buildEmptyBoard({})


def printBoard(board: dict):
    lineV = "%s|%s|%s"
    lineH = "-+-+-"
    print(lineV % (board[topL], board[topM], board[topR]))
    print(lineH)
    print(lineV % (board[midL], board[midM], board[midR]))
    print(lineH)
    print(lineV % (board[lowL], board[lowM], board[lowR]))


def moveChecked(board, move) -> bool:
    return move in board and board[move] == defValue


def checkWinner(board: dict, turn: str):
    winsPos = [
        [topL, topM, topR],
        [topL, midL, lowL],
        [topM, midM, lowM],
        [topR, midR, lowR],
        [midL, midM, midR],
        [lowL, lowM, lowR],
        # diags
        [topL, midM, lowR],
        [topR, midM, lowL],
    ]

    for winPos in winsPos:
        boardElements = list(board[pos] for pos in winPos)
        res = reduce(lambda x, y: x == turn and y, boardElements)
        if res == turn:
            return turn
    return defValue


turn = "X"
hasWinner = False
printBoard(board)
for i in range(9):
    cellNotEmpty = True
    while cellNotEmpty:
        print("Move for %s cell?" % (turn), end=": ")
        move = input()
        cellNotEmpty = not moveChecked(board, move)
    board[move] = turn
    printBoard(board)
    hasWinner = checkWinner(board, turn) == turn
    if hasWinner:
        print(f"{turn} is WON")
        break
    turn = "O" if turn == "X" else "X"
if not hasWinner:
    print("DRAW!")


# TESTS

"""
if __name__ == "__main__":
    board = buildEmptyBoard({})
    checkMove1 = moveChecked(board, topL)
    assert checkMove1
    assert not moveChecked(board, "ddd"), "Key not found in a board"

    # top 3X
    board1 = board | {topL: turnX, topM: turnX, topR: turnX, midL: turnO, lowL: turnO}
    printBoard(board1)
    winner = checkWinner(board1, turnX)
    assert winner == turnX, "Incorect winner O"
    assert not moveChecked(board1, topL)
    assert moveChecked(board1, lowR)
    # left 3X
    board2 = board | {topL: turnX, topM: turnO, topR: turnO, midL: turnX, lowL: turnX}
    winner2 = checkWinner(board2, turnX)
    assert winner2 == turnX, "Incorrect winner O"
    assert winner2 != turnO, "O didn't win"
    assert not moveChecked(board2, topM)
    assert not moveChecked(board2, "ddd")
    assert moveChecked(board2, midM)
    # diag left-right
    board3 = board | {topL: turnO, midM: turnO, lowR: turnO}
    winner3 = checkWinner(board3, turnO)
    assert winner3 == turnO, "Incorrect winner X"
    assert winner3 != turnX, "Winner X didn't win"
    assert moveChecked(board3, topM)
    assert not moveChecked(board3, topL)
    # diag rigth-left
    board4 = board | {topR: turnO, midM: turnO, lowL: turnO}
    winner4 = checkWinner(board4, turnO)
    assert winner4 == turnO, "Incorrect winner X"
    assert winner4 != turnX, "Winner X didn't win"
    assert winner4 != defValue
    assert moveChecked(board4, topM)
    assert moveChecked(board4, midL)
    assert not moveChecked(board4, topR)
    # right 3X
    board5 = board | {topR: turnX, midR: turnX, lowR: turnX}
    winner5 = checkWinner(board5, turnX)
    assert winner5 == turnX, "Incorrect winner O"
    assert moveChecked(board5, topL)
    assert moveChecked(board5, midM)
    assert not moveChecked(board5, topR)
    # mid 3O
    board6 = board | {midL: turnO, midM: turnO, midR: turnO}
    winner6 = checkWinner(board6, turnO)
    assert winner6 == turnO, "Incorrect winner"
    assert moveChecked(board6, topR)
    assert moveChecked(board6, lowL)
    assert not moveChecked(board6, midR)
    # low 3X
    board7 = board | {lowL: turnX, lowM: turnX, lowR: turnX}
    winner7 = checkWinner(board7, turnX)
    assert winner7 == turnX, "Incorrect winner O"
    assert moveChecked(board7, midR)
    assert moveChecked(board7, topR)
    assert not moveChecked(board7, lowM)
"""
