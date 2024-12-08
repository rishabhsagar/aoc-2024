from collections import defaultdict
import re

def validate_and_correct_manual_order(file_name):
    with open(file_name, 'r') as f:
        puzzle_input = f.read()

    rules, updates = puzzle_input.split('\n\n')

    page_dependencies = defaultdict(set)
    for p1, p2 in re.findall(r'(\d+)\|(\d+)', rules):
        page_dependencies[int(p2)].add(int(p1))

    def calculate_middle_page(pages):
        blocked_pages = set()
        for page in pages:
            if page in blocked_pages:
                return 0
            blocked_pages |= page_dependencies[page]

        return pages[len(pages) // 2]

    def topological_sort(pages):
        in_degree = {page: 0 for page in pages}
        graph = {page: [] for page in pages}

        for page in pages:
            for dependency in page_dependencies[page]:
                if dependency in pages:
                    graph[dependency].append(page)
                    in_degree[page] += 1

        queue = [page for page in pages if in_degree[page] == 0]
        sorted_pages = []

        while queue:
            current = queue.pop(0)
            sorted_pages.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_pages if len(sorted_pages) == len(pages) else []

    total_valid = 0
    total_corrected = 0

    for line in updates.strip().split('\n'):
        pages = list(map(int, line.split(',')))
        middle_page = calculate_middle_page(pages)
        if middle_page > 0:
            total_valid += middle_page
        else:
            corrected_order = topological_sort(pages)
            if corrected_order:
                total_corrected += corrected_order[len(corrected_order) // 2]

    return total_valid, total_corrected

if __name__ == "__main__":
    file_name = "input.txt"
    valid_total, corrected_total = validate_and_correct_manual_order(file_name)
    print(f"Total score of valid updates: {valid_total}")
    print(f"Total score of corrected updates: {corrected_total}")
