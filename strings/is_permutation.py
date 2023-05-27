"""
Is Permutation: Given two strings, write a method to decide if one is a permutation of the other.

Author: Fuzzy Carter
"""

from function_timer import function_timer


@function_timer
def is_permutation_oridianl_sum(s1: str, s2: str):
    """
    Check if is permutation by comparing the sum of the ordinal values of each character in the string.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param s1: The first string to compare.
    :param s2: The second string to compare.
    :return: True if the strings are permutations of each other.
    """

    if len(s1) != len(s2):
        return False

    sum1 = 0
    sum2 = 0

    for i in range(len(s1)):
        sum1 += ord(s1[i])
        sum2 += ord(s2[i])

    return sum1 == sum2


@function_timer
def is_permutation_string_minus_string(s1: str, s2: str):
    """
    Check if is permutation by subtracting one string from the other.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param s1: The first string to compare.
    :param s2: The second string to compare.
    :return: True if the strings are permutations of each other.
    """

    if len(s1) != len(s2):
        return False

    result = sum(map(ord, s1)) - sum(map(ord, s2))

    return result == 0


@function_timer
def is_permutation_string_equal_string(s1: str, s2: str):
    """
    Check if is permutation by comparing the strings.

    Time Complexity: O(n log(n))
    Space Complexity: O(1)

    
    :param s1: The first string to compare.
    :param s2: The second string to compare.  
    :return: True if the strings are permutations of each other.
    """

    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


@function_timer
def is_permutation_character_count(s1: str, s2: str):
    """
    Check if is permutation by counting the characters.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param s1: The first string to compare.
    :param s2: The second string to compare.
    :return: True if the strings are permutations of each other.
    """

    if len(s1) != len(s2):
        return False

    char_count = [0] * 128

    for char in s1:
        char_count[ord(char)] += 1

    for char in s2:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False

    return True

if __name__ == "__main__":
    string_permutation_true_1 = "abcdefghi"
    string_permutation_true_2 = "ihgfedcba"

    string_permutation_false_1 = "abcdefghi"
    string_permutation_false_2 = "ihgfedcbz"

    print(is_permutation_oridianl_sum(string_permutation_true_1, string_permutation_true_2))
    print(is_permutation_oridianl_sum(string_permutation_false_1, string_permutation_false_2))

    print(is_permutation_string_minus_string(string_permutation_true_1, string_permutation_true_2))
    print(is_permutation_string_minus_string(string_permutation_false_1, string_permutation_false_2))

    print(is_permutation_string_equal_string(string_permutation_true_1, string_permutation_true_2))
    print(is_permutation_string_equal_string(string_permutation_false_1, string_permutation_false_2))

    print(is_permutation_character_count(string_permutation_true_1, string_permutation_true_2))
    print(is_permutation_character_count(string_permutation_false_1, string_permutation_false_2))
