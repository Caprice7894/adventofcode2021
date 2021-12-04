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
    winnerid = -1
    winnerNum = -1
    colid = -1
    rowid = -1
    for number in numbers:
        for boardid in range(len(boards)):
            for row in range(len(boards[boardid])):
                for col in range(len(boards[boardid][row])):
                    if number == boards[boardid][row][col]:
                        markeds[boardid][row][col] = 1
                        rowid = fetch_winner_row(markeds[boardid])
                        cowid = fetch_winner_col(markeds[boardid])
            if colid != -1 or rowid != -1:
                winnerid = boardid
                winnerNum = number
                break
        if winnerid != -1:
            break
    score(winnerid, winnerNum)

def score(boardid, winnerNum):
    score = 0
    for row in range(len(boards[boardid])):
        for col in range(len(boards[boardid][row])):
            if markeds[boardid][row][col] == 1:
                continue
            score += boards[boardid][row][col]
    print(score * winnerNum)

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
    for col in range(len(board[0])):
        count = 0
        for row in range(len(board)):
            if board[row][col] == 0:
                break
            count += board[col][row]
        if count == len(board):
            return col
    return -1


mark()
