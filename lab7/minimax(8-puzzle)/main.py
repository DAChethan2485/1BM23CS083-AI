import heapq

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x, y = divmod(val - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def valid(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def copy_state(state):
    return [row[:] for row in state]

def serialize(state):
    return tuple(tuple(row) for row in state)

def solve(start):
    open_list = []
    heapq.heappush(open_list, (manhattan(start), 0, start, []))
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        if state == goal_state:
            return path + [state]
        visited.add(serialize(state))
        x, y = find_zero(state)
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if valid(nx, ny):
                new_state = copy_state(state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                if serialize(new_state) not in visited:
                    heapq.heappush(open_list, (g + 1 + manhattan(new_state), g + 1, new_state, path + [state]))
    return None

def print_path(path):
    for state in path:
        for row in state:
            print(row)
        print()

if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 6],
             [7, 5, 8]]
    path = solve(start)
    if path:
        print("Solution found in", len(path) - 1, "moves:")
        print_path(path)
    else:
        print("No solution found.")
