def count_safe_reports(filename):
    def is_safe_report(levels):
        direction = None
        for i in range(len(levels) - 1):
            diff = levels[i + 1] - levels[i]
            if not (1 <= abs(diff) <= 3):
                return False
            if direction is None:
                if diff > 0:
                    direction = "increasing"
                elif diff < 0:
                    direction = "decreasing"
            elif (direction == "increasing" and diff <= 0) or (direction == "decreasing" and diff >= 0):
                return False
        return True

    with open(filename, 'r') as file:
        reports = [list(map(int, line.split())) for line in file]

    return sum(1 for report in reports if is_safe_report(report))

if __name__ == "__main__":
    safe_report_count = count_safe_reports("input.txt")
    print(f"Total safe reports: {safe_report_count}")