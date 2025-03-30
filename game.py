import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column 0-2): ").split())
            if (row, col) in get_available_moves(board):
                board[row][col] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter two numbers between 0 and 2.")

def computer_move(board):
    row, col = random.choice(get_available_moves(board))
    board[row][col] = "O"
    print(f"Computer placed 'O' at ({row}, {col})")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe: You are 'X', Computer is 'O'")
    print_board(board)
    
    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
