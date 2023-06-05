"""
Zero Matrix

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

Solution 1: Use Boolean Arrays to track rows and columns set to zero
Solution 2: Use Boolean Arrays to track rows and columns set to zero (Pythonic)
Solution 2: Use Source Matrix to track rows and columns set to zero

Author: Fuzzy Carter
"""
from copy import deepcopy

from function_timer import function_timer
from string_helpers import printable_matrix


@function_timer
def zero_matrix_boolean_arrays(matrix: list[list]) -> list[list]:
    """
    Zero out rows and columns that contain a zero.

    Iterate through the matrix and set the corresponding row and column in the boolean arrays to True. Iterate through
    the matrix again and zero out the rows and columns that are set to True.

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    This solution is the same as zero_matrix_boolean_arrays_pythonic() but is less Pythonic and more verbose.
    """
    rows = [False] * len(matrix)
    columns = [False] * len(matrix[0])

    # Store the row and column index with value 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 0:
                rows[row] = True
                columns[column] = True

    # Zero out rows
    for row in range(len(rows)):
        if rows[row]:
            zero_out_row(matrix, row)

    # Zero out columns
    for column in range(len(columns)):
        if columns[column]:
            zero_out_column(matrix, column)

    return matrix


@function_timer
def zero_matrix_boolean_arrays_pythonic(matrix: list[list]) -> list[list]:
    """
    Zero out rows and columns that contain a zero.

    Iterate through the matrix and set the corresponding row and column in the boolean arrays to True. Iterate through
    the matrix again and zero out the rows and columns that are set to True.

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    This solution is the same as zero_matrix_boolean_arrays() but is more Pythonic.
    """

    # Store the row and column index with value 0
    rows = [row for row in range(len(matrix)) for column in range(len(matrix[row])) if matrix[row][column] == 0]
    columns = [column for row in range(len(matrix)) for column in range(len(matrix[row])) if matrix[row][column] == 0]

    # Zero out rows
    for row in rows:
        zero_out_row(matrix, row)

    # Zero out columns
    for column in columns:
        zero_out_column(matrix, column)

    return matrix


@function_timer
def zero_matrix_source_matrix(matrix: list[list]) -> list[list]:
    """
    Zero out rows and columns that contain a zero.

    1.Check if the first row and column contain a zero.
    2.Iterate through the matrix, setting matrix[i][0] and matrix[0][j] to zero whenever there's a zero in matrix[i][j].
    3.Iterate through the matrix, nullifying row i if there's a zero in matrix[i][0].
    4.Iterate through the first column, nullifying column j if there's a zero in matrix[0][j].
    5.Nullify the first row and column if necessary.

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    This solution has the same time complexity as zero_matrix_boolean_arrays() but has a space complexity of O(1) since
    it uses the source matrix to track rows and columns set to zero. While it has the same time complexity as the other
    solutions, it is overall faster than the other solutions. This is because it does not have to create and iterate
    through the boolean arrays.

    This solution is a little harder to understand than the other solutions but provides space complexity improvements
    for when space is a concern.
    """
    first_row_zero = first_row_has_zero(matrix)
    first_column_zero = first_column_has_zero(matrix)

    # Check if the rest of the matrix has zeros and zero them out
    matrix_has_zeros(matrix)
    zero_out_columns(matrix)
    zero_out_rows(matrix)

    # Zero out first row and column if necessary
    zero_out_first_column_row(first_row_zero, first_column_zero, matrix)

    return matrix


# -- Helper Functions ---------------------------------------------------------


def zero_out_row(matrix: list[list], row: int) -> None:
    """
    Zero out a row in a matrix.
    """
    for column in range(len(matrix[row])):
        matrix[row][column] = 0


def zero_out_rows(matrix: list[list]) -> None:
    """
    Zero out +1 index rows in a matrix.
    """
    for row in range(1, len(matrix)):
        if matrix[row][0] == 0:
            zero_out_row(matrix, row)


def zero_out_column(matrix: list[list], column: int) -> None:
    """
    Zero out a column in a matrix.
    """
    for row in range(len(matrix)):
        matrix[row][column] = 0


def zero_out_columns(matrix: list[list]) -> None:
    """
    Zero out +1 index columns in a matrix.
    """
    for column in range(1, len(matrix[0])):
        if matrix[0][column] == 0:
            zero_out_column(matrix, column)


def first_row_has_zero(matrix: list[list]) -> bool:
    """
    Check if the first row of a matrix has a zero.
    """
    for column in range(len(matrix[0])):
        if matrix[0][column] == 0:
            return True
    return False


def first_column_has_zero(matrix: list[list]) -> bool:
    """
    Check if the first column of a matrix has a zero.
    """
    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            return True
    return False


def zero_out_first_column_row(first_row_zero: bool, first_column_zero: bool, matrix: list[list]) -> None:
    """
    Zero out the first row and column of a matrix if necessary.
    """
    if first_row_zero:
        zero_out_row(matrix, 0)

    if first_column_zero:
        zero_out_column(matrix, 0)


def matrix_has_zeros(matrix: list[list]) -> None:
    """
    Check for zeros in the rest of the matrix and update the first row and column.
    """

    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[row])):
            if matrix[row][column] == 0:
                matrix[0][column] = 0
                matrix[row][0] = 0


# -- Main ---------------------------------------------------------------------

if __name__ == "__main__":
    test_matrix_3_3 = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]
    test_matrix_3_4 = [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 11, 12]
    ]
    test_matrix_5_5 = [
        [1, 2, 3, 4, 5],
        [6, 7, 0, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

    print("Zero Matrix - Boolean Arrays Tests")
    print("==================================")
    print(f"Original Matrix 3x3: {printable_matrix(test_matrix_3_3)}"
          f"Zeroed Matrix 3x3: {printable_matrix(zero_matrix_boolean_arrays(deepcopy(test_matrix_3_3)))}")
    print(f"Original Matrix 3x4: {printable_matrix(test_matrix_3_4)}"
          f"Zeroed Matrix 3x4: {printable_matrix(zero_matrix_boolean_arrays(deepcopy(test_matrix_3_4)))}")
    print(f"Original Matrix 5x5: {printable_matrix(test_matrix_5_5)}"
          f"Zeroed Matrix 5x5: {printable_matrix(zero_matrix_boolean_arrays(deepcopy(test_matrix_5_5)))}")

    print("\nZero Matrix - Boolean Arrays Pythonic Tests")
    print("============================================")
    print(f"Original Matrix 3x3: {printable_matrix(test_matrix_3_3)}"
          f"Zeroed Matrix 3x3: {printable_matrix(zero_matrix_boolean_arrays_pythonic(deepcopy(test_matrix_3_3)))}")
    print(f"Original Matrix 3x4: {printable_matrix(test_matrix_3_4)}"
          f"Zeroed Matrix 3x4: {printable_matrix(zero_matrix_boolean_arrays_pythonic(deepcopy(test_matrix_3_4)))}")
    print(f"Original Matrix 5x5: {printable_matrix(test_matrix_5_5)}"
          f"Zeroed Matrix 5x5: {printable_matrix(zero_matrix_boolean_arrays_pythonic(deepcopy(test_matrix_5_5)))}")

    print("\nZero Matrix - Source Matrix Tests")
    print("==================================")
    print(f"Original Matrix 3x3: {printable_matrix(test_matrix_3_3)}"
          f"Zeroed Matrix 3x3: {printable_matrix(zero_matrix_source_matrix(deepcopy(test_matrix_3_3)))}")
    print(f"Original Matrix 3x4: {printable_matrix(test_matrix_3_4)}"
          f"Zeroed Matrix 3x4: {printable_matrix(zero_matrix_source_matrix(deepcopy(test_matrix_3_4)))}")
    print(f"Original Matrix 5x5: {printable_matrix(test_matrix_5_5)}"
          f"Zeroed Matrix 5x5: {printable_matrix(zero_matrix_source_matrix(deepcopy(test_matrix_5_5)))}")
