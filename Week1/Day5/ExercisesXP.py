def display_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def player_input(player, board):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position! Please enter 0-2.")
                continue
            
            if board[row][col] != " ":
                print("That position is taken!")
                continue
            
            return row, col
        except ValueError:
            print("Please enter valid numbers!")

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        display_board(board)
        row, col = player_input(current_player, board)
        board[row][col] = current_player
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

play()