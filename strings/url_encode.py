"""
URL Encode: Given a string, replace non-leading or trailing spaces with '%20' and removing all others.

Author: Fuzzy Carter
"""

from function_timer import function_timer

@function_timer
def url_encode(string: str):
    """
    Encode a string for a URL by iterating through each character in the string and replacing spaces with '%20'. Handles
    leading and trailing spaces by removing them.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param string: The string to encode.
    :return: The encoded string.
    """
    string = string.strip()

    encoded_string = ""

    for char in string:
        if char == " ":
            encoded_string += "%20"
        else:
            encoded_string += char

    return encoded_string


@function_timer
def url_encode_pythonic(string: str):
    """
    Encode a string for a URL by using the built-in replace function to replace spaces with '%20'. Handles leading and
    trailing spaces by removing them.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param string: The string to encode.
    :return: The encoded string.
    """
    string = string.strip()

    return string.replace(" ", "%20")


if __name__ == "__main__":
    string_to_encode = "   Hello World!   "
    string_to_encode2 = "HelloWorld ! World     Hello"

    print(url_encode(string_to_encode))
    print(url_encode(string_to_encode2))

    print(url_encode_pythonic(string_to_encode))
    print(url_encode_pythonic(string_to_encode2))
