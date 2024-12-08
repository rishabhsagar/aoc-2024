def count_xmas_patterns(file_path):
    with open(file_path, 'r') as file:
        rows = file.read().splitlines()

    m = len(rows)
    n = len(rows[0]) if rows else 0

    def count(r, c):
        if rows[r][c] != 'X':
            return 0
        directions = [
            [(0, -i) for i in range(4)],  # left
            [(0, i) for i in range(4)],   # right
            [(-i, 0) for i in range(4)],  # up
            [(i, 0) for i in range(4)],   # down
            [(-i, -i) for i in range(4)], # left-up
            [(-i, i) for i in range(4)],  # right-up
            [(i, -i) for i in range(4)],  # left-down
            [(i, i) for i in range(4)]    # right-down
        ]
        count = 0
        for direction in directions:
            try:
                if all(0 <= r+dr < m and 0 <= c+dc < n and rows[r+dr][c+dc] == "XMAS"[i] for i, (dr, dc) in enumerate(direction)):
                    count += 1
            except IndexError:
                continue
        return count

    return sum(count(r, c) for r in range(m) for c in range(n))


if __name__ == "__main__":
    fn = "input.txt"
    print(f"Total: {count_xmas_patterns(fn)}")
