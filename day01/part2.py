from collections import Counter


def sim_score(file_name):
    column1, column2 = [], []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                col1, col2 = map(int, parts)
                column1.append(col1)
                column2.append(col2)

    count_right = Counter(column2)
    similarity_score = sum(num * count_right[num] for num in column1)

    return similarity_score

if __name__ == "__main__":
    print(sim_score("input.txt"))