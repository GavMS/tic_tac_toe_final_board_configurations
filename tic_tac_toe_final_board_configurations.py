from itertools import combinations, permutations

print_move_final_board = False

def check_winner(board):
    # Define winning combinations
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]
    
    # Check for winner
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] != ' ':
            return True
    return False


def print_board(board):
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print()

print("===========================================")

def count_5_move_final_board():
    positions = range(9)
    five_move_final_board = 0
    
    # Iterate over all possible positions for 'X'
    for x_positions in combinations(positions, 3):
        # Create a board and place 'X'
        board = [' ']*9
        for pos in x_positions:
            board[pos] = 'X'
        
        # Iterate over all possible positions for 'O'
        for o_positions in combinations(set(positions) - set(x_positions), 2):
            # Place 'O' on the board
            for pos in o_positions:
                board[pos] = 'O'
            
            # Check if there's a winner
            if check_winner(board):
                five_move_final_board += 1
                if (print_move_final_board == True):
                    print("Final board (5 moves):")
                    print_board(board)
            
            # Reset 'O' positions for next iteration
            for pos in o_positions:
                board[pos] = ' '
    
    return five_move_final_board

result = count_5_move_final_board()

# Calculate and print the number of 5-move final boards

print(f"The number of 5-move final boards (3 'X' and 2 'O'): {result}")


def is_valid_x_positions(x_positions):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]

    for win in wins:
        if set(win).issubset(x_positions):
            return False
    return True

def count_6_move_final_board():
    positions = range(9)
    six_move_final_board = 0
    unique_configurations = set()

    # Iterate over all possible positions for 'X'
    for x_positions in combinations(positions, 3):
        if not is_valid_x_positions(x_positions):
            continue

        # Create a board and place 'X'
        board = [' ']*9
        for pos in x_positions:
            board[pos] = 'X'

        # Iterate over all possible positions for 'O'
        for o_positions in combinations(set(positions) - set(x_positions), 3):
            # Place 'O' on the board
            for pos in o_positions:
                board[pos] = 'O'

            # Check if there's a winner
            if check_winner(board):
                # Convert the board configuration to a tuple for hashing
                board_tuple = tuple(board)
                if board_tuple not in unique_configurations:
                    unique_configurations.add(board_tuple)
                    six_move_final_board += 1

                    if (print_move_final_board == True):
                        print("Final board (6 moves):")
                        print_board(board)

            # Reset 'O' positions for next iteration
            for pos in o_positions:
                board[pos] = ' '

    return six_move_final_board

# Calculate and print the number of 6-move final boards
result = count_6_move_final_board()
print(f"The number of 6-move final boards (3 'X' and 3 'O'): {result}")

def count_7_move_final_board():
    positions = range(9)
    seven_move_final_board = 0
    unique_configurations = set()

    # Iterate over all possible positions for 'X' (3 moves)
    for x_positions in combinations(positions, 3):
        if not is_valid_x_positions(x_positions):  # Ensure X doesn't already win
            continue

        # Create a board and place 'X'
        board = [' '] * 9
        for pos in x_positions:
            board[pos] = 'X'

        # Iterate over all possible positions for the first 3 moves of 'O'
        for o_positions in combinations(set(positions) - set(x_positions), 3):
            if not is_valid_x_positions(o_positions):  # Ensure O doesn't already win
                continue

            # Place the first 3 'O' on the board
            for pos in o_positions:
                board[pos] = 'O'

            # Iterate over remaining positions for the 4th move of 'O'
            for remaining_pos in set(positions) - set(x_positions) - set(o_positions):
                board[remaining_pos] = 'O'  # Place the 4th 'O'

                # Check if there's a winner (O winning after 4 moves)
                if check_winner(board):
                    # Convert the board configuration to a tuple for hashing
                    board_tuple = tuple(board)
                    if board_tuple not in unique_configurations:
                        unique_configurations.add(board_tuple)
                        seven_move_final_board += 1
                        if (print_move_final_board == True):
                            print("Final board (7 moves):")
                            print_board(board)

                board[remaining_pos] = ' '  # Reset the 4th 'O' for the next iteration

            # Reset the first 3 'O' positions for the next iteration
            for pos in o_positions:
                board[pos] = ' '

    return seven_move_final_board

# Calculate and print the number of 7-move final boards
result = count_7_move_final_board()
print(f"The number of 7-move final boards (3 'X' and 4 'O'): {result}")

def count_8_move_final_board():
    positions = range(9)
    eight_move_final_board = 0
    unique_configurations = set()

    # Iterate over all possible positions for 'X' (4 moves)
    for x_positions in combinations(positions, 4):
        if not is_valid_x_positions(x_positions):  # Ensure X doesn't already win
            continue

        # Create a board and place 'X'
        board = [' '] * 9
        for pos in x_positions:
            board[pos] = 'X'

        # Iterate over all possible positions for 'O' (4 moves)
        for o_positions in combinations(set(positions) - set(x_positions), 4):
            # Place 'O' on the board
            for pos in o_positions:
                board[pos] = 'O'

            # Check if there's a winner (either X or O wins)
            if check_winner(board):
                # Convert the board configuration to a tuple for hashing
                board_tuple = tuple(board)
                if board_tuple not in unique_configurations:
                    unique_configurations.add(board_tuple)
                    eight_move_final_board += 1
                    if (print_move_final_board == True):
                        print("Final board (8 moves):")
                        print_board(board)

            # Reset 'O' positions for the next iteration
            for pos in o_positions:
                board[pos] = ' '

    return eight_move_final_board

# Calculate and print the number of 8-move final boards
result = count_8_move_final_board()
print(f"The number of 8-move final boards (4 'X' and 4 'O'): {result}")

def count_9_move_final_board_and_ties():
    positions = range(9)
    nine_move_final_board = 0
    tie_final_board = 0
    unique_configurations = set()

    # Iterate over all possible positions for 'O' (4 moves)
    for o_positions in combinations(positions, 4):
        if not is_valid_x_positions(o_positions):  # Ensure O doesn't already win
            continue

        # Create a board and place 'O'
        board = [' '] * 9
        for pos in o_positions:
            board[pos] = 'O'

        # Iterate over all possible positions for 'X' (5 moves)
        for x_positions in combinations(set(positions) - set(o_positions), 5):
            # Place 'X' on the board
            for pos in x_positions:
                board[pos] = 'X'

            # Check for winner or tie
            if check_winner(board):
                # Convert the board configuration to a tuple for hashing
                board_tuple = tuple(board)
                if board_tuple not in unique_configurations:
                    unique_configurations.add(board_tuple)
                    nine_move_final_board += 1
                    if (print_move_final_board == True):
                        print("Final board (9 moves):")
                        print_board(board)
            else:
                # Check for tie game (no winner and board is full)
                if all(cell != ' ' for cell in board):
                    tie_final_board += 1
                    if (print_move_final_board == True):
                        print("Tie game:")
                        print_board(board)

            # Reset 'X' positions for the next iteration
            for pos in x_positions:
                board[pos] = ' '

    return nine_move_final_board, tie_final_board

# Calculate and print the number of 9-move final boards and ties
nine_move_wins, ties = count_9_move_final_board_and_ties()
print(f"The number of 9-move final boards (4 'O' and 5 'X') where someone wins: {nine_move_wins}")
print(f"The number of tie final board (4 'O' and 5 'X'): {ties}")

print("===========================================")
total = count_5_move_final_board() + count_6_move_final_board() + count_7_move_final_board() + count_8_move_final_board() + nine_move_wins + ties

print("Total final board configurations = ", total)

print("===========================================")

print_move_final_board = True

while True:
    print("\nTic-Tac-Toe Board Configurations Menu\n")
    print("1. Print 5-move final boards")
    print("2. Print 6-move final boards")
    print("3. Print 7-move final boards")
    print("4. Print 8-move final boards")
    print("5. Print 9-move final boards (wins and ties)")
    print("6. Print total final board configurations")
    print("7. Exit\n")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        count_5_move_final_board()
    elif choice == '2':
        count_6_move_final_board()
    elif choice == '3':
        count_7_move_final_board()
    elif choice == '4':
        count_8_move_final_board()
    elif choice == '5':
        nine_move_wins, ties = count_9_move_final_board_and_ties()
    elif choice == '6':
        print_total_configurations()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")
