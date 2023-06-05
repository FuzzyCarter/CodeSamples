"""
Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer, write a
method to rotate the image by 90 degrees.

Can you do this in place?

Example:
Input:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Output:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

Solution 1: Transpose and Reverse
Solution 2: Rotate Groups of Four Cells
Solution 3: Rotate One Cell at a Time

Hint 51: Try thinking about it layer by layer. Can you rotate a specific layer?
Hint 100: Rotating a specific layer would just mean swapping the values in four arrays. If you were asked to swap the
        values in two arrays, could you do this? Can you then extend it to four arrays?

Author: Fuzzy Carter


"""

from function_timer import function_timer
from string_helpers import printable_matrix

@function_timer
def rotate_matrix_groups_of_four(original_matrix: list[list]) -> list:
    """
    Rotate the matrix by rotating groups of four cells.

    Iterate through the matrix and rotate each group of four cells. The first cell in the group is the top cell and
    will be stored in a temporary variable. The top cell is replaced by the left cell, the left cell is replaced by the
    bottom cell, the bottom cell is replaced by the right cell, the right cell is replaced by the temporary variable.

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    This solution is the most efficient solution because it only requires one pass through the matrix and does not
    require any additional space.
    """
    for layer in range(len(original_matrix) // 2):
        first = layer
        last = len(original_matrix) - layer - 1

        for i in range(first, last):
            offset = i - first
            top = original_matrix[first][i]

            # Left -> Top
            original_matrix[first][i] = original_matrix[last - offset][first]

            # Bottom -> Left
            original_matrix[last - offset][first] = original_matrix[last][last - offset]

            # Right -> Bottom
            original_matrix[last][last - offset] = original_matrix[i][last]

            # Top -> Right
            original_matrix[i][last] = top

    return original_matrix

@function_timer
def rotate_matrix_transpose_and_reverse(original_matrix: list[list]) -> list:
    """
    Rotate the matrix by first transposing the matrix and then reversing each row.

    Transpose the matrix by swapping the rows and columns. Reverse each row by swapping the first element with the last
    element, the second element with the second to last element, and so on.

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    This solution is the least efficient solution because it requires two passes through the matrix.
    """
    # Transpose the matrix
    for row in range(len(original_matrix)):
        for col in range(row, len(original_matrix)):
            original_matrix[row][col], original_matrix[col][row] = original_matrix[col][row], original_matrix[row][col]

    # Reverse each row
    for row in range(len(original_matrix)):
        for col in range(len(original_matrix) // 2):
            original_matrix[row][col], original_matrix[row][len(original_matrix) - col - 1] = original_matrix[row][
                len(original_matrix) - col - 1], original_matrix[row][col]

    return original_matrix


@function_timer
def rotate_matrix_one_cell_at_a_time(original_matrix: list[list]) -> list:
    """
    Rotate the matrix by rotating one cell at a time.

    Rotate the matrix by rotating one cell at a time. Rotate the top left cell with the top right cell, the top right
    cell with the bottom right cell, the bottom right cell with the bottom left cell, and the bottom left cell with the
    top left cell. Move to the next cell and repeat the process until the entire matrix is rotated.

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    This solution is similar to the rotate_matrix_groups_of_four() solution, but it is not as efficient because it
    requires more operations per iteration. However, it is easier to understand.
    """
    for row in range(len(original_matrix) // 2):
        for col in range(row, len(original_matrix) - row - 1):
            top_left = original_matrix[row][col]
            top_right = original_matrix[col][len(original_matrix) - row - 1]
            bottom_right = original_matrix[len(original_matrix) - row - 1][len(original_matrix) - col - 1]
            bottom_left = original_matrix[len(original_matrix) - col - 1][row]

            original_matrix[row][col] = bottom_left
            original_matrix[col][len(original_matrix) - row - 1] = top_left
            original_matrix[len(original_matrix) - row - 1][len(original_matrix) - col - 1] = top_right
            original_matrix[len(original_matrix) - col - 1][row] = bottom_right

    return original_matrix


if __name__ == "__main__":
    example_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    large_matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

    print("Transposed and Reversed Matrix Tests:")
    print(f"Example Matrix: {printable_matrix(example_matrix)} \n"
          f"Rotated Example Matrix: {printable_matrix(rotate_matrix_transpose_and_reverse(example_matrix))}")
    print(f"Large Matrix: {printable_matrix(large_matrix)} \n"
          f"Rotated Large Matrix: {printable_matrix(rotate_matrix_transpose_and_reverse(large_matrix))}")

    print("\nGroups of Four Matrix Tests:")
    print(f"Example Matrix: {printable_matrix(example_matrix)} \n"
          f"Rotated Example Matrix: {printable_matrix(rotate_matrix_groups_of_four(example_matrix))}")
    print(f"Large Matrix: {printable_matrix(large_matrix)} \n"
          f"Rotated Large Matrix: {printable_matrix(rotate_matrix_groups_of_four(large_matrix))}")

    print("\nOne Cell at a Time Matrix Tests:")
    print(f"Example Matrix: {printable_matrix(example_matrix)} \n"
          f"Rotated Example Matrix: {printable_matrix(rotate_matrix_one_cell_at_a_time(example_matrix))}")
    print(f"Large Matrix: {printable_matrix(large_matrix)} \n"
            f"Rotated Large Matrix: {printable_matrix(rotate_matrix_one_cell_at_a_time(large_matrix))}")
