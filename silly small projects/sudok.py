import sys

def getInsideIndex(position):
    row = position[0]
    col = position[1]

    if col in (1,4,7):
        index = 3 + (row % 3)
    if col in (2,5,8):
        index = 6 + (row % 3)
    if col in (0,3,6):
        index = row % 3
    return index

def getBoxIndex(pos):
    """ Find which box a position is in"""
    if pos[1] < 3 and pos[0] < 3:
        return 0
    if 2 < pos[1] < 6 and pos[0] < 3:
        return 1
    if 5 < pos[1] and pos[0] < 3:
        return 2
    if pos[1] < 3 and 2 < pos[0] < 6:
        return 3
    if 2 < pos[1] < 6 and 2 < pos[0] < 6:
        return 4
    if 5 < pos[1] and 2 < pos[0] < 6:
        return 5
    if pos[1] < 3 and 5 < pos[0]:
        return 6
    if 2 < pos[1] < 6 and 5 < pos[0]:
        return 7
    if 5 < pos[1] and 5 < pos[0]:
        return 8


def getBoxes(board):
    """ Gets the 9 boxes of a Sudoku board left to right, top to bottom"""
    boxes = []
    ranges = [(0, 2), (3, 5), (6, 8)]

    for g in ranges:
        for r in ranges:
            box_row = []
            for x in range(r[0], r[1] + 1):
                for y in range(g[0], g[1] + 1):
                    box_row.append(board[y][x])
                    if y == g[1] and x == r[1]:
                        boxes.append(box_row)
    return boxes


def getColumns(board):
    """ Gets the 9 columns of a Sudoku board """
    columns = []
    for x in range(9):
        col = []
        for y in range(9):
            col.append(board[y][x])
            if y == 8:
                columns.append(col)
    return columns


def possible(num, pos, row, column, box):
    """ Checks whether a placement is valid in a sudoku board"""
    if str(num) in row[pos[0]]:
        return False
    if str(num) in column[pos[1]]:
        return False
    if str(num) in box[getBoxIndex(pos)]:
        return False
    return True


def solve(sudoku):
    "implementing backtracking algorithm"
    # gets a sudoku board, line by line, from user

    numbers_tried = {}
    # gets the positions of the blank spots and sets them to a dictionary where we'll see which numbers we've tried.
    positions = []
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == '.':
                positions.append((r, c))
                numbers_tried[(r, c)] = 1

    rows = [k[:] for k in sudoku]
    columns = getColumns(sudoku)
    boxes = getBoxes(sudoku)

    pointer = 0
    while True:
        if pointer < 0:
            break
        if pointer == len(positions):
            break

        location = positions[pointer]

        sudoku[location[0]][location[1]] = '.'
        columns[location[1]][location[0]] = '.'
        rows[location[0]][location[1]] = '.'
        boxes[getBoxIndex(location)][getInsideIndex(location)] = '.'

        num_to_try = numbers_tried[location]

        if num_to_try > 9:
            pointer -= 1
            numbers_tried[location] = 1
            continue

        if possible(num_to_try, location, rows, columns, boxes):
            sudoku[location[0]][location[1]] = str(num_to_try)
            columns[location[1]][location[0]] = str(num_to_try)
            rows[location[0]][location[1]] = str(num_to_try)
            boxes[getBoxIndex(location)][getInsideIndex(location)] = str(num_to_try)

            pointer += 1
            numbers_tried[location] += 1
            continue

        if num_to_try != 9:
            numbers_tried[location] += 1
        else:
            numbers_tried[location] = 1
            pointer -= 1

    return sudoku


if __name__ == 'main':
    solve()
