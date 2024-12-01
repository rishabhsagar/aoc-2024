def sum_of_differences(file_name):
    column1, column2 = [], []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                col1, col2 = map(int, parts)
                column1.append(col1)
                column2.append(col2)
    column1.sort()
    column2.sort()
    return sum(abs(a - b) for a, b in zip(column1, column2))


if __name__ == "__main__":
    print(sum_of_differences("test.txt"))