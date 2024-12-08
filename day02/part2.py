def count_safe_reports_new(filename):
    def is_safe_report(levels):
        direction = None
        for i in range(len(levels) - 1):
            diff = levels[i+1] - levels[i]
            if not (1 <= abs(diff) <= 3):
                return False
            if direction is None:
                direction = "increasing" if diff > 0 else "decreasing"
            elif (direction == "increasing" and diff <= 0) or (direction == "decreasing" and diff >= 0):
                return False
        return True

    def is_safe_new(levels):
        if is_safe_report(levels):
            return True
        for i in range(len(levels)):
            if is_safe_report(levels[:i] + levels[i+1:]):
                return True
        return False

    with open(filename, 'r') as file:
        reports = [list(map(int, line.split())) for line in file if line.strip()]

    return sum(is_safe_new(report) for report in reports)

if __name__ == "__main__":
    safe_report_count = count_safe_reports_new("input.txt")
    print(f"Total safe reports: {safe_report_count}")
