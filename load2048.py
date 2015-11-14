import pickle

def load(range):
    boards = []
    moves = []
    for i in xrange(range):
        with open('training_data'+str(i), 'rb') as f:
            training_data = pickle.load(f)
            boards.append(training_data[0])
            moves.append(training_data[1])
    flattened_boards = [board for sublist in boards for board in sublist]
    flattened_moves = [move for sublist in moves for move in sublist]
    return [flattened_boards, flattened_moves]

def scale_boards(boards, log=True):
    for i, board in enumerate(boards):
        scale(board, log)
    return boards

def scale(board, log):
    highest_value = 0
    for j, val in enumerate(board):
        if val > highest_value:
            highest_value = val
    if log:
        board/highest_value
    else:
        board = 2**board
    return board




cases = load(1)
boards = cases[0]
moves = cases[1]

print(boards[0])
test_board = scale(boards[0], True)
print(test_board)


