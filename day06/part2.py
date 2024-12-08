from collections import defaultdict
from bisect import insort, bisect

def solve_guard_path(file_path):
    def parse_map(file_path):
        with open(file_path, 'r') as f:
            grid = [line.strip() for line in f.readlines()]

        m, n = len(grid), len(grid[0])
        obstacles = {
            'rows': defaultdict(list),
            'cols': defaultdict(list),
        }
        start = None
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '#':
                    insort(obstacles['rows'][r], c)
                    insort(obstacles['cols'][c], r)
                if grid[r][c] == '^':
                    start = (r, c, 'up')
        return grid, obstacles, start, m, n

    def move(r, c, d, obstacles):
        r_obs = obstacles['rows'][r]
        c_obs = obstacles['cols'][c]

        if d == 'up':
            if not c_obs or c_obs[0] > r:
                new_r = -1
            else:
                i = bisect(c_obs, r)
                new_r = c_obs[i-1] + 1
            return new_r, c, 'right'

        if d == 'right':
            if not r_obs or r_obs[-1] < c:
                new_c = n
            else:
                i = bisect(r_obs, c)
                new_c = r_obs[i] - 1
            return r, new_c, 'down'

        if d == 'down':
            if not c_obs or c_obs[-1] < r:
                new_r = m
            else:
                i = bisect(c_obs, r)
                new_r = c_obs[i] - 1
            return new_r, c, 'left'

        if d == 'left':
            if not r_obs or r_obs[0] > c:
                new_c = -1
            else:
                i = bisect(r_obs, c)
                new_c = r_obs[i-1] + 1
            return r, new_c, 'up'

    def is_looping(obstacles):
        r, c, d = start
        visited = set([(r, c, d)])
        while r in range(m) and c in range(n):
            r, c, d = move(r, c, d, obstacles)
            if (r, c, d) in visited:
                return True
            visited.add((r, c, d))
        return False

    grid, obstacles, start, m, n = parse_map(file_path)

    candidates = set()
    r, c, d = start
    while r in range(m) and c in range(n):
        new_r, new_c, new_d = move(r, c, d, obstacles)
        if d == 'up':
            candidates |= set((i, c) for i in range(new_r + 1, r + 1))
        elif d == 'right':
            candidates |= set((r, j) for j in range(c, new_c))
        elif d == 'down':
            candidates |= set((i, c) for i in range(r, new_r))
        elif d == 'left':
            candidates |= set((r, j) for j in range(new_c + 1, c + 1))
        r, c, d = new_r, new_c, new_d

    loop_count = 0
    for r, c in candidates:
        insort(obstacles['rows'][r], c)
        insort(obstacles['cols'][c], r)
        if is_looping(obstacles):
            loop_count += 1
        obstacles['rows'][r].remove(c)
        obstacles['cols'][c].remove(r)

    return loop_count

if __name__ == "__main__":
    file_path = "input.txt"
    print(solve_guard_path(file_path))
