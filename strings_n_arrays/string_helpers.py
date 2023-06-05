"""
A place to store helper functions for working with strings.
"""

def printable_matrix(matrix: list[list]) -> str:
    """
    Return a string representation of the matrix for easy printing.
    """
    printable_matrix = "\n"
    for row in matrix:
        printable_matrix += f"{row}\n"

    return printable_matrix