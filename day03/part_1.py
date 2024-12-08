import re

def f(fname: str) -> int:
    p = r"mul\((\d+),(\d+)\)"
    s = 0
    with open(fname, 'r') as f:
        for l in f:
            for x, y in re.findall(p, l):
                s += int(x) * int(y)
    return s

if __name__ == "__main__":
    fn = "input.txt"
    print(f"Total: {f(fn)}")
