import random

def create_board(size=4):
    if size % 2 != 0:
        raise ValueError("Size must be an even number")

    cards = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUU')
    random.shuffle(cards)
    board = [cards[i:i + size] for i in range(0, len(cards), size)]
    return board

def display_board(board, revealed):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if revealed[row][col]:
                print(board[row][col], end=' ')
            else:
                print('_', end=' ')
        print()

def select_card():
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    return row, col

def memory_puzzle():
    size = 4  # 4x4 board
    board = create_board(size)
    revealed = [[False] * size for _ in range(size)]
    moves = 0

    while True:
        display_board(board, revealed)
        print("Select the first card.")
        row1, col1 = select_card()
        revealed[row1][col1] = True
        display_board(board, revealed)

        print("Select the second card.")
        row2, col2 = select_card()
        if (row1, col1) == (row2, col2):
            print("You selected the same card. Choose a different card.")
            continue

        revealed[row2][col2] = True
        display_board(board, revealed)

        if board[row1][col1] != board[row2][col2]:
            print("Not a match.")
            revealed[row1][col1] = False
            revealed[row2][col2] = False
        else:
            print("It's a match!")

        moves += 1
        if all(all(row) for row in revealed):
            print(f"Congratulations! You completed the game in {moves} moves.")
            break
        else:
            input("Press Enter to continue...")

if __name__ == "__main__":
    memory_puzzle()
