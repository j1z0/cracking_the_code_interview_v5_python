'''
design and algorithm to figure out if someone has won tic-tac-toe
3 horizontal 
3 vertical
3 diagnol
'''

def col_row_winner(board):

    for j in range(3):
        #test row
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
        
        if board[j][0] == board[j][1] == board[j][2]:
            return board[j][0]


    return None


def diag_winner(board):

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][0]

    return None


def and_the_winner_is(board):
    '''
    board should be 3x3 matrix wth
    string values x and o
    '''

    winner = col_row_winner(board)
    if winner: return winner

    winner = diag_winner(board)
    if winner: return winner

    return "cat"
        

if __name__ == "__main__":
    board = [['x','o',''],
             ['x','o','x'],
             ['x','','o']]

    print(and_the_winner_is(board))

    board = [['x','o',''],
             ['o','o','o'],
             ['x','','o']]

    print(and_the_winner_is(board))

    board = [['x','o',''],
             ['o','x','o'],
             ['x','','x']]

    print(and_the_winner_is(board))


    board = [['x','o',''],
             ['o','','o'],
             ['x','','x']]

    print(and_the_winner_is(board))

