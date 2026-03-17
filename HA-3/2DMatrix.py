import math
from xmlrpc.client import boolean


def matrix(matrix: list[list[int]], target: int) -> tuple[int, int] | boolean:
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return row, col
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False


# Test Cases
matrix1 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target1 = 5
print(f"Expected: (1, 1), Got: {matrix(matrix1, target1)}")  # Expected Output: (1, 1)

matrix2 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target2 = 20
print(f"Expected: False, Got: {matrix(matrix2, target2)}")  # Expected Output: False

matrix3 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target3 = 1
print(f"Expected: (0, 0), Got: {matrix(matrix3, target3)}")  # Expected Output: (0, 0)
