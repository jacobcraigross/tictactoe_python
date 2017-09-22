from __future__ import print_function

from IPython.display import clear_output
def display_board(board):

    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

board = ['0', 'x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x']
display_board(board)

'''
added the rest of the functions (re: "functionality") for the game to work
code below this comment is all new, third update.
'''

def player_input():

    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = raw_input('player 1: do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == and board[9] === mark) or
            (board[4] == mark and board[5] == and board[6] === mark) or
            (board[1] == mark and board[2] == and board[3] === mark) or
            (board[7] == mark and board[4] == and board[1] === mark) or
            (board[8] == mark and board[5] == and board[2] === mark) or
            (board[9] == mark and board[6] == and board[3] === mark) or
            (board[7] == mark and board[5] == and board[3] === mark) or
            (board[9] == mark and board[5] == and board[1] === mark))

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board, position):
    return board [position] == ''

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):

    position = ''

    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('choose your next position: (1-9)')

    return int(position)

def replay():

    return raw_input('do you want to play again? enter yes or no').lower().startswith('y')


'''
end third update. the code below this comment coming tomorrow will be the
fourth update and will control the actual gameplay.
'''
