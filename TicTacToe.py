import random

def display_board(board):
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('----------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('----------')
    print(board[1]+' | '+board[2]+' | '+board[3])

def player_input():
    print('WELCOME TO TIC TAC TOE!')
    marker=' '
    while marker not in ['X','O']:
        marker =input('Player1: Do you want to be X or O ?').upper()
        if marker not in ['X','O']:
            print("Sorry, but you did not choose a valid value (X,O)")
    if marker =='X':
        return ('X','O')
    else:
        return ('O','X')
    
def place_marker(board, marker, position):
    board[position]=marker   

def win_check(board, mark):
    return ((board[7]== mark and board[8]==mark and board[9]== mark) or
    (board[4]== mark and board[5]== mark and board[6]== mark) or
    (board[1]== mark and board[2]== mark and board[3]== mark) or
    (board[7]== mark and board[4]== mark and board[1]== mark) or
    (board[8]== mark and board[5]== mark and board[2]== mark) or
    (board[9]== mark and board[6]== mark and board[3]== mark) or
    (board[7]== mark and board[5]== mark and board[3]== mark) or
    (board[9]== mark and board[5]== mark and board[1]== mark))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in range (0,10):
        if space_check(board,i):
            return False
    return True     

def player_choice(board):
    position= 0
    while position not in range (1,10) or not space_check(board, position):
        position= int(input('Chose your next position: (1-9)'))
    return position

def replay():
    return input ('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

while True:
    test_board = [' ']*10
    player1Marker , player2Marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Y or N.')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(test_board)
            position= player_choice(test_board)
            place_marker(test_board, player1Marker ,position)

            if win_check(test_board,player1Marker):
                display_board(test_board)
                print ('PLAYER 1 HAS WON')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print ('TIE GAME')
                else:
                    turn = 'Player 2'
                    
        # Player2's turn.
        else:
            display_board(test_board)
            position= player_choice(test_board)
            place_marker(test_board, player2Marker ,position)

            if win_check(test_board,player2Marker):
                display_board(test_board)
                print ('PLAYER 2 HAS WON')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print ('TIE GAME')
                else:
                    turn = 'Player 1'
              
    if not replay():
        break  