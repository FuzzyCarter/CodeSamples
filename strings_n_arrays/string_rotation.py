"""
String Rotation

Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2,
write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of
"erbottlewat")

Author: Fuzzy Carter
"""

from function_timer import function_timer


@function_timer
def is_rotation(string1: str, string2: str) -> bool:
    """
    Checks if string2 is a rotation of string1.

    Time Complexity: O(n)
    Space Complexity: O(n)

    This works since a rotation will always be a substring of the original string concatenated with itself.
    """
    if len(string1) != len(string2):
        return False

    return is_substring(string1 + string1, string2)


# -- Helper Functions ---------------------------------------------------------

def is_substring(string1: str, string2: str) -> bool:
    """
    Checks if string2 is a substring of string1.
    """
    return string2 in string1


# -- Main ---------------------------------------------------------------------
if __name__ == '__main__':
    test_string1 = "waterbottle"
    test_string2 = "erbottlewat"

    test_string_fail = "waterbottles"

    print(f"Is {test_string2} a rotation of {test_string1}? {is_rotation(test_string1, test_string2)}")
    print(f"Is {test_string_fail} a rotation of {test_string1}? {is_rotation(test_string1, test_string_fail)}")
