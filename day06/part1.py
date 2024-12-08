def solve_guard_path(file_path):
    def parse_map(file_path):
        with open(file_path, 'r') as f:
            grid = [list(line.strip()) for line in f.readlines()]

        direction_map = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell in direction_map:
                    return grid, (y, x), cell

        raise ValueError("Guard's starting position not found in the map.")

    def is_within_bounds(pos, rows, cols):
        y, x = pos
        return 0 <= y < rows and 0 <= x < cols

    grid, guard_pos, direction = parse_map(file_path)
    rows, cols = len(grid), len(grid[0])

    direction_map = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    visited = set()
    visited.add(guard_pos)

    while True:
        dy, dx = direction_map[direction]
        next_pos = (guard_pos[0] + dy, guard_pos[1] + dx)

        if not is_within_bounds(next_pos, rows, cols):
            break

        next_y, next_x = next_pos
        if grid[next_y][next_x] == '#':
            direction = right_turn[direction]
        else:
            guard_pos = next_pos
            visited.add(guard_pos)

    return len(visited)

if __name__ == "__main__":
    file_path = "input.txt"
    print(solve_guard_path(file_path))
