#! /bin/python3
archivo = open("dia4/dia4.txt", "r")
lines = []
line = archivo.readline()

numbers = line.rstrip("\n")
numbers = line.split(",")
numbers = [int(x) for x in numbers]

boards = []
markeds = []

i = -1
for line in archivo:
    line = line.rstrip("\n")
    if line == "":
        i += 1
        boards.append([])
        markeds.append([])
    else:
        row = line.split(" ")
        boards[i].append([int(x) for x in row if len(x) > 0])
        markeds[i].append([0 for x in row if len(x) > 0])

def mark():
    saveState = []
    winNumber = -1
    winnerBoard = []
    for number in numbers:
        for i in range(len(boards)):
            if i in winnerBoard:
                continue
            board = boards[i]
            _row = -1
            _col = -1
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == number:
                        markeds[i][row][col] = 1
                        _col = fetch_winner_col(markeds[i])
                        _row = fetch_winner_row(markeds[i])
                if _col > -1:
                    break
            if _row > -1 or _col > -1:
                winNumber = number
                winnerBoard.append(i)
                saveState = [boards[i], markeds[i], winNumber]
        
        if len(boards) == 1:
            break

    score([saveState[0],saveState[1]],saveState[2])

#edita el score para que se ajuste a el arreglo
def score(boards, winnerNum):
    score = 0
    for row in range(len(boards[0])):
        for col in range(len(boards[0][row])):
            if boards[1][row][col] == 1:
                continue
            score += boards[0][row][col]
    print(score * winnerNum, ",", score, ",", winnerNum)


def fetch_winner_row(board):
    for row in range(len(board)):
        count = 0
        for col in range(len(board[0])):
            if board[row][col] == 0:
                break
            count += board[row][col]
        if count == len(board[0]):
            return row
    return -1

def fetch_winner_col(board):
    for col in range(len(board)):
        count = 0
        for row in range(len(board)):
            if board[row][col] == 0:
                break
            count += board[row][col]
        if count == len(board):
            return col
    return -1


mark()
