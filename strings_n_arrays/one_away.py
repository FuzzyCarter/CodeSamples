"""
One Away: There are three types of edits that can be performed on strings_n_arrays: insert a character, remove a character, or
replace a character. Given two strings_n_arrays, write a function to check if they are one edit (or zero edits) away.

Example:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

Author: Fuzzy Carter
"""

from function_timer import function_timer


@function_timer
def one_away_cleaner(first_string: str, second_string: str) -> bool:
    """
    Check if is one away by iterating through the strings_n_arrays and comparing the characters. If the characters are different,
    check if the strings_n_arrays are one insert, one remove, or one replace away from being equal. If the characters are the
    same, continue iterating through the strings_n_arrays.

    This solution is cleaner than the one_away_single_loop solution but is less efficient because it performs two
    different loops through the strings_n_arrays for improved readability.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param first_string: The first string to compare.
    :param second_string: The second string to compare.
    :return: True if the strings_n_arrays are one edit away from being equal.
    """

    if len(first_string) == len(second_string):
        return one_replace_away(first_string, second_string)
    elif len(first_string) + 1 > len(second_string):
        return one_insert_away(first_string, second_string)
    elif len(first_string) - 1 < len(second_string):
        return one_insert_away(second_string, first_string)

    return False


@function_timer
def one_away_single_loop(first_string: str, second_string: str) -> bool:
    """
    Check if is one insert away by iterating through the strings_n_arrays and comparing the characters and performing the insert,
    remove, or replace check all in the same loop.

    This solution is less clean than the one_away_cleaner solution but is more efficient because it performs only one
    loop through the strings_n_arrays. However, it is less readable than the one_away_cleaner solution.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param first_string: The first string to compare.
    :param second_string: The second string to compare.
    :return: True if the strings_n_arrays are one edit away from being equal.
    """
    if abs(len(first_string) - len(second_string)) > 1:
        return False

    # Get the shorter and longer string.
    shorter_string = first_string if len(first_string) < len(second_string) else second_string
    longer_string = second_string if len(first_string) < len(second_string) else first_string

    index1 = 0
    index2 = 0
    found_difference = False

    # Iterate through both strings_n_arrays and compare the characters.
    # If the characters are different, toggle found_difference to true.
    # If the characters are different and found_difference is true, return False.
    while index1 < len(shorter_string) and index2 < len(longer_string):
        if shorter_string[index1] != longer_string[index2]:
            if found_difference:
                return False

            found_difference = True

            if len(shorter_string) == len(longer_string):
                index1 += 1
        else:
            index1 += 1

        index2 += 1

    return True


# -- Helper Functions ---------------------------------------------------------

def one_replace_away(first_string: str, second_string: str) -> bool:
    """
    Check if is one replace away by iterating through the strings_n_arrays and comparing the characters. If the characters are
    different, toggle found_differences to true. If the characters are different and found_differences is true, return
    False.

    :param first_string: The first string to compare.
    :param second_string: The second string to compare.
    :return: True if the strings_n_arrays are one replace away from being equal.
    """
    found_difference = False

    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            if found_difference:
                return False

            found_difference = True

    return True


def one_insert_away(first_string: str, second_string: str) -> bool:
    """
    Check if is one insert away by iterating through the strings_n_arrays and comparing the characters. If the characters are
    different and indices are the same, increment one of the indices. If the indices are different, and the characters
    are different, return False.

    :param first_string: The first string to compare.
    :param second_string: The second string to compare.
    :return: True if the strings_n_arrays are one insert away from being equal.
    """
    char_1_index = 0
    char_2_index = 0

    while char_1_index < len(first_string) and char_2_index < len(second_string):
        if first_string[char_1_index] != second_string[char_2_index]:
            if char_1_index != char_2_index:
                return False

            char_2_index += 1
        else:
            char_1_index += 1
            char_2_index += 1

    return True


if __name__ == "__main__":
    one_away_true1 = "pale"
    one_away_true2 = "pales"
    one_away_true3 = "bale"
    one_away_true4 = "ale"

    one_away_false = "bake"
    one_away_large_false = "bakery"
    one_away_small_false = "ke"

    print(f"one_away_cleaner Tests:")
    print(f"{one_away_true1} is one away from {one_away_true2} should be true: "
          f"{one_away_cleaner(one_away_true1, one_away_true2)}")
    print(f"{one_away_true1} is one away from {one_away_true3} should be true: "
          f"{one_away_cleaner(one_away_true1, one_away_true3)}")
    print(f"{one_away_true1} is one away from {one_away_true4} should be true: "
          f"{one_away_cleaner(one_away_true1, one_away_true4)}")

    print(f"{one_away_false} is one away from {one_away_small_false} should be false: "
          f"{one_away_cleaner(one_away_true1, one_away_small_false)}")
    print(f"{one_away_false} is one away from {one_away_large_false} should be false: "
          f"{one_away_cleaner(one_away_true1, one_away_large_false)}")

    print(f"\none_away_single_loop Tests:")
    print(f"{one_away_true1} is one away from {one_away_true2} should be true: "
          f"{one_away_single_loop(one_away_true1, one_away_true2)}")
    print(f"{one_away_true1} is one away from {one_away_true3} should be true: "
          f"{one_away_single_loop(one_away_true1, one_away_true3)}")
    print(f"{one_away_true1} is one away from {one_away_true4} should be true: "
          f"{one_away_single_loop(one_away_true1, one_away_true4)}")

    print(f"{one_away_false} is one away from {one_away_small_false} should be false: "
          f"{one_away_single_loop(one_away_true1, one_away_small_false)}")
    print(f"{one_away_false} is one away from {one_away_large_false} should be false: "
          f"{one_away_single_loop(one_away_true1, one_away_large_false)}")
