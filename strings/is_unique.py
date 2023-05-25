"""
Is Unique String: Implement an algorithm to determine if a string has all unique characters.

Additionally, what if you cannot use additional data structures?
"""

from function_timer import function_timer

@function_timer
def is_unique_no_ds(string: str):
    """
    Using no additional data structures without sorting.

    Compare each character to every other character.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    if is_ascii(string):
        return False

    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

@function_timer
def is_unique_no_ds_sorted(string: str):
    """
    Using no additional data structures but can modify the string.

    Sort the string and compare each character to the next.

    Time Complexity: O(n log(n))
    Space Complexity: O(1)
    """
    if is_ascii(string):
        return False

    string = sorted(string)
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True

@function_timer
def is_unique_set(string: str):
    """
    Using a set to keep track of characters seen.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if is_ascii(string):
        return False

    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

@function_timer
def is_unique_bool(string: str):
    """
    Using a boolean array to keep track of characters seen.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if is_ascii(string):
        return False

    char_set = [False] * 128
    for char in string:
        if char_set[ord(char)]:
            return False
        char_set[ord(char)] = True
    return True

def is_ascii(string: str):
    """
    Checks if a string is ASCII.
    """
    return len(string) > 128


if __name__ == "__main__":
    test_unique_string = "abcdefg"
    test_non_unique_string = "abcdefga"
    test_129_char_string = "a" * 129
    test_unique_128_char_ascii_string = "".join([chr(i) for i in range(128)])

    print(is_unique_no_ds(test_unique_string), end="\n\n")
    print(is_unique_no_ds(test_non_unique_string), end="\n\n")
    print(is_unique_no_ds(test_129_char_string), end="\n\n")
    print(is_unique_no_ds(test_unique_128_char_ascii_string), end="\n\n")

    print(is_unique_no_ds_sorted(test_unique_string), end="\n\n")
    print(is_unique_no_ds_sorted(test_non_unique_string), end="\n\n")
    print(is_unique_no_ds_sorted(test_129_char_string), end="\n\n")
    print(is_unique_no_ds_sorted(test_unique_128_char_ascii_string), end="\n\n")

    print(is_unique_bool(test_unique_string), end="\n\n")
    print(is_unique_bool(test_non_unique_string), end="\n\n")
    print(is_unique_bool(test_129_char_string), end="\n\n")
    print(is_unique_bool(test_unique_128_char_ascii_string), end="\n\n")

    print(is_unique_set(test_unique_string), end="\n\n")
    print(is_unique_set(test_non_unique_string), end="\n\n")
    print(is_unique_set(test_129_char_string), end="\n\n")
    print(is_unique_set(test_unique_128_char_ascii_string), end="\n\n")
