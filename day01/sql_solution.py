import sqlite3

def load_file_into_sqlite(file_name):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE numbers (col1 INTEGER, col2 INTEGER)')
    with open(file_name, 'r') as file:
        data = [tuple(map(int, line.split())) for line in file if line.strip()]
        cursor.executemany('INSERT INTO numbers (col1, col2) VALUES (?, ?)', data)
    conn.commit()
    return conn

def calculate_similarity_score_sql(file_name):
    conn = load_file_into_sqlite(file_name)
    cursor = conn.cursor()
    query = '''
        SELECT SUM(col1 * count)
        FROM (
            SELECT n.col1, COUNT(n2.col2) as count
            FROM numbers n
            LEFT JOIN numbers as n2 ON n.col1 = n2.col2
            GROUP BY n.col1
        )
    '''
    cursor.execute(query)
    result = cursor.fetchone()[0]
    conn.close()
    return result

def sod_sql(file_name):
    conn = load_file_into_sqlite(file_name)
    cursor = conn.cursor()
    query = '''
        WITH sorted_col1 AS (
            SELECT col1, ROW_NUMBER() OVER (ORDER BY col1) as rn1
            FROM numbers
        ),
        sorted_col2 AS (
            SELECT col2, ROW_NUMBER() OVER (ORDER BY col2) as rn2
            FROM numbers
        )
        SELECT SUM(ABS(sorted_col1.col1 - sorted_col2.col2))
        FROM sorted_col1
        JOIN sorted_col2 ON sorted_col1.rn1 = sorted_col2.rn2
    '''
    cursor.execute(query)
    result = cursor.fetchone()[0]
    conn.close()
    return result

if __name__ == "__main__":
    file_name = "input.txt"
    similarity_score = calculate_similarity_score_sql(file_name)
    print("Similarity Score:", similarity_score)
    difference_sum = sod_sql(file_name)
    print("Sum of Differences:", difference_sum)
