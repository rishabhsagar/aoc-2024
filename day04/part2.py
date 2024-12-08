def count_x_mas_patterns(file_path):
    with open(file_path, 'r') as file:
        rows = file.read().splitlines()

    m = len(rows)
    n = len(rows[0]) if rows else 0

    def check(r, c):
        if rows[r][c] != 'A':
            return False
        ul = rows[r-1][c-1]
        ur = rows[r-1][c+1]
        dl = rows[r+1][c-1]
        dr = rows[r+1][c+1]
        return sorted([ul, ur, dl, dr]) == ['M', 'M', 'S', 'S'] and ul != dr

    return sum(check(r, c) for r in range(1, m-1) for c in range(1, n-1))

if __name__ == "__main__":
    input_file = "input.txt"
    print(count_x_mas_patterns(input_file))