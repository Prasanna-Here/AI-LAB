def print_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board,current_player):
    win_conditions=[
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)    
    ]

    for a,b,c in win_conditions:
        if board[a]==board[b]==board[c]==current_player:
            return True
    return False

def tic_tac_toe():
    board=['-']*9
    current_player='X'

    print_board(board)

    for _ in range(9):
        print(f"{current_player}'s Turn")
        pos=int(input("Enter position from 1-9: "))
        board[pos-1]=current_player
        print_board(board)

        if check_winner(board,current_player):
            print(f"Player {current_player} wins!")
            return
        
        current_player='O' if current_player=='X' else 'X'
    
    print("Draw")

tic_tac_toe()