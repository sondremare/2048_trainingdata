import pickle
import numpy as np

training_data_start = 0
training_data_end = 25
testing_data_start = training_data_end
testing_data_end = 33

def load(start, stop):
    boards = []
    moves = []
    for i in range(start, stop):
        with open('training_data'+str(i), 'rb') as f:
            training_data = pickle.load(f)
            boards.append(training_data[0])
            moves.append(training_data[1])
    flattened_boards = [board for sublist in boards for board in sublist]
    flattened_moves = [move for sublist in moves for move in sublist]
    return [np.array(flattened_boards), np.array(flattened_moves)]

def scale_boards(boards, log2):
    for i, board in enumerate(boards):
        board = scale(board, log2)
    return boards

def scale(board, log2):
    highest_value = 0.0
    for j, val in enumerate(board):
        if val > highest_value:
            highest_value = val
    if log2:
        board = board/highest_value
    else:
        board = (2**board)/(2**highest_value)
    return board

def load_training_data(log2=True):
    data = load(training_data_start, training_data_end)
    boards = scale_boards(data[0], log2)
    moves = data[1]
    print("Training data loaded, "+str(len(boards))+" cases")
    return boards, moves


def load_testing_data(log2=True):
    data = load(testing_data_start, testing_data_end)
    boards = scale_boards(data[0], log2)
    moves = data[1]
    print("Testing data loaded, "+str(len(boards))+" cases")
    return boards, moves

load_training_data()
load_testing_data()