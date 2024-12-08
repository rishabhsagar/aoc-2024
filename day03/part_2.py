import re


def sum_in_scope_mul(file_path):
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_pattern = r"mul\((\d+),(\d+)\)"
    total_sum = 0
    enabled = True
    with open(file_path, 'r') as file:
        for line in file:
            for match in re.finditer(f'{do_pattern}|{dont_pattern}|{mul_pattern}', line):
                if re.fullmatch(do_pattern, match.group()):
                    enabled = True
                elif re.fullmatch(dont_pattern, match.group()):
                    enabled = False
                elif enabled:
                    mul_match = re.fullmatch(mul_pattern, match.group())
                    if mul_match:
                        total_sum += int(mul_match.group(1)) * int(mul_match.group(2))
    return total_sum

if __name__ == "__main__":
    fn = "input.txt"
    print(f"Total: {sum_in_scope_mul(fn)}")
