# define the function to decide players' symbols
def sym():
    symbol_1 = input("Player 1, do you want to be X or O? ")
    while symbol_1 not in ["X", "O"]:
        symbol_1 = input("Invalid input. Please enter X or O: ")
    if symbol_1 == "X":
        symbol_2 = "O"
    else:
        symbol_2 = "X"
    print(f"Player 1 is {symbol_1}. Player 2 is {symbol_2}.")
    return symbol_1, symbol_2

# define the board
board = [["_" for i in range(3)] for j in range(3)]

# define the player's move
def make_move(board, player, row, col):
  if board[row][col] == "_":
    board[row][col] = player
  else:
    print("That spot is already occupied. Pick a different spot")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    make_move(board, player, row, col)
    
# define the function to check for a winner
def check_winner(board):
  # check rows
  for row in range(3):
    if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
      return board[row][0]

  # check columns
  for col in range(3):
    if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
      return board[0][col]

  # check diagonals
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
    return board[0][0]
  if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
    return board[2][0]

  # if there is no winner, return None
  return None

# define the function to check if the game is a draw
def check_draw(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == "_":
        return False
  return True

# define the function to play the game

def play_game():
    # initialize the game
    symbol_1, symbol_2 = sym()
    player = symbol_1
    winner = None
    draw = False

    # loop until the game is over
    while not winner and not draw:
        # print the current board
        for row in board:
            print(" ".join(row))

        # get the player's move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
                   
        # make the move
        make_move(board, player, row, col)

        # check for a winner
        winner = check_winner(board)

        # check for a draw
        draw = check_draw(board)

        # switch players
        if player == "X":
            player = "O"
        else:
            player = "X"

    # print the final board
    for row in board:
        print(" ".join(row))

    # print the result of the game
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("The game is a draw.")
        
    # define the function to ask if the user wants to play again
    def play_again():
        answer = input("Do you want to play again? (Y/N) ")
        while answer not in ["Y", "N"]:
            answer = input("Invalid input. Please enter Y or N: ")
        return answer == "Y"

    # loop until the user doesn't want to play anymore
    while True:
        # play the game
        play_game()

        # ask if the user wants to play again
        if not play_again():
            break

# play the game
play_game()
