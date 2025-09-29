def print_board(board):
    # Print the game board
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("---------")

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in range(3):
        if all([cell == player for cell in board[row]]):  # Check row
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):  # Check column
            return True

    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check other diagonal
        return True

    return False

def check_draw(board):
    # Check if the game is a draw (board is full)
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def play_tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'")
    
    # Create a 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Start the game loop
    current_player = "X"  # Player 1 starts
    while True:
        print_board(board)
        
        # Get player input
        try:
            row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1
            
            if board[row][col] != " ":
                print("This spot is already taken! Try again.")
                continue
            
            # Place the mark on the board
            board[row][col] = current_player

            # Check for win or draw
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column numbers between 1 and 3.")

# Run the game
play_tic_tac_toe()
