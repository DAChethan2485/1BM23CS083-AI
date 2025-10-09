import random

def calculate_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_neighbors(board):
    neighbors = []
    n = len(board)
    for col in range(n):
        for row in range(n):
            if board[col] != row:
                new_board = list(board)
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            line += " Q " if board[col] == row else " . "
        print(line)
    print()

def hill_climbing(n):
    current = [random.randint(0, n - 1) for _ in range(n)]
    current_h = calculate_conflicts(current)
    step = 0

    print(f"Initial state (heuristic={current_h}):")
    print_board(current)

    while current_h != 0:
        neighbors = get_neighbors(current)
        neighbor_h = [(calculate_conflicts(neighbor), neighbor) for neighbor in neighbors]
        neighbor_h.sort(key=lambda x: x[0])

        if neighbor_h[0][0] >= current_h:
            # Restart with new random board if stuck
            current = [random.randint(0, n - 1) for _ in range(n)]
            current_h = calculate_conflicts(current)
            print(f"Restarting with new initial state (heuristic={current_h}):")
            print_board(current)
            step = 0
            continue

        current_h = neighbor_h[0][0]
        current = neighbor_h[0][1]
        step += 1
        print(f"Step {step} (heuristic={current_h}):")
        print_board(current)

    return current, current_h

solution, heuristic = hill_climbing(4)
print("Final solution:")
print_board(solution)
print("Final heuristic:", heuristic)
