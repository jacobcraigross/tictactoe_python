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
