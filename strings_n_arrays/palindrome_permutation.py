"""
Given a string, write a function to check if it is a permutation of a palindrome.

A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

You can ignore casing and non-letter characters.

Example: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)

Author: Fuzzy Carter
"""

from string import ascii_lowercase
from typing import Dict
from function_timer import function_timer


@function_timer
def is_palindrome_permutation_hash_table(phrase: str) -> bool:
    """
    Check if is palindrome permutation by using a hash table to count the number of times each character appears in the
    string. Then, iterate through the hash table and count the number of characters that appear an odd number of times.
    If more than one character appears an odd number of times, return False.

    Time Complexity: O(n)
    Space Complexity: O(n)
    
    :param phrase: The potential palindrome permutation.
    :return: True if the string is a palindrome permutation.
    """

    character_count = get_char_frequency(phrase)
    return check_max_one_odd_character(character_count)


@function_timer
def is_palindrome_permutation_odd_count(phrase: str) -> bool:
    """
    Check if is palindrome permutation by keeping track of the number of characters that appear an odd number of times.

    This solution has similar time and space complexity to is_palindrome_permutation_hash_table, but could be more
    efficient because it does not require iterating through the hash table to count the number of characters that appear
    an odd number of times. However, this solution is less readable and has more operations per character and could wind
    up being less efficient in some cases.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param phrase: The potential palindrome permutation.
    :return: True if only one character appears an odd number of times
    """

    odd_count = 0
    character_count = {}

    for char in phrase:
        char = char.lower()

        if char in ascii_lowercase:
            character_count[char] = character_count.get(char, 0) + 1

            if character_count.get(char) % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1

    return odd_count <= 1


@function_timer
def is_palindrome_permutation_bit_vector(phrase: str) -> bool:
    """
    Check if is palindrome permutation by using a bit vector to keep track if the character count is odd or even.

    This solution has a better space complexity than other solutions but is less readable and uses more complex bit
    logic for those gains. This solution should only be used where space is a premium.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param phrase:
    :return:
    """

    bit_vector = 0

    for char in phrase:
        char = char.lower()

        if char in ascii_lowercase:
            char_ordinal = ord(char)
            bit_vector = toggle_bit(bit_vector, char_ordinal)

    return check_max_one_bit_set(bit_vector)


# -- Helper Functions ---------------------------------------------------------

def get_char_frequency(phrase: str) -> dict:
    """
    Get the frequency of each character in the string.

    This function will not count non-letter characters and treat upper and lower case characters as the same.

    :param phrase:
    :return: A dictionary containing the frequency of each character in the string.
    """
    character_count = {}

    for char in phrase:
        char = char.lower()

        if char in ascii_lowercase:  # Ignore non-letter characters.
            character_count[char] = character_count.get(char, 0) + 1

    return character_count


def check_max_one_odd_character(character_count: Dict[str, int]) -> bool:
    """
    Check if there is more than one character that appears an odd number of times.

    :param character_count: A dictionary containing the frequency of each character in the string.
    :return: True if there is at most one character that appears an odd number of times.
    """
    odd_count = 0

    for char in character_count:
        if character_count[char] % 2 != 0:
            odd_count += 1

    return odd_count <= 1


def toggle_bit(bit_vector: int, index: int) -> int:
    """
    Toggle the bit at the given index in the bit vector.

    :param bit_vector: The bit vector to toggle the bit in.
    :param index: The index of the bit to toggle.
    :return: The bit vector with the bit at the given index toggled.
    """
    if index < 0:
        return bit_vector

    mask = 1 << index  # Create a mask with a 1 at the given index and 0s everywhere else.
    bit_vector ^= mask  # XOR the bit vector with the mask to toggle the bit at the given index.

    return bit_vector


def check_max_one_bit_set(bit_vector: int) -> bool:
    """
    Check if there is at most one bit set in the bit vector.

    Subtracting 1 from a number with only one bit set will result in a number with all bits to the right of the set
    bit set and all bits to the left of the set bit unset. ANDing the original number with the result of
    subtracting 1 from the original number will result in 0 if there is only one bit set in the original number.

    :param bit_vector: The bit vector to check.
    :return: True if there is at most one bit set in the bit vector.
    """
    return (bit_vector & (bit_vector - 1)) == 0


if __name__ == "__main__":
    phrase_even_true = "k a aky"
    palindrome_permutation_odd_true = "Tact Coa"
    palindrome_permutation_non_letter_odd_true = "$%^&*()_++Tact Coa!##  .,<>/?~`][}{]"

    palindrome_permutation_odd_false = "Tact Coaa"
    palindrome_permutation_non_letter_odd_false = "$%^&*()_++car!RaCec##  .,<>/?~`][}{]"

    print(f"The following strings test is_palindrome_permutation_hash_table.")
    print(f"Palindrome Permutation Even True: {is_palindrome_permutation_hash_table(phrase_even_true)}")
    print(f"Palindrome Permutation Odd True: {is_palindrome_permutation_hash_table(palindrome_permutation_odd_true)}")
    print(f"Palindrome Permutation Non-Letter Odd True: "
          f"{is_palindrome_permutation_hash_table(palindrome_permutation_non_letter_odd_true)}")
    print(f"Palindrome Permutation Odd False: {is_palindrome_permutation_hash_table(palindrome_permutation_odd_false)}")
    print(f"Palindrome Permutation Non-Letter Odd False: "
          f"{is_palindrome_permutation_hash_table(palindrome_permutation_non_letter_odd_false)}")

    print(f"\nThe following strings test is_palindrome_permutation_odd_count.")
    print(f"Palindrome Permutation Even True: {is_palindrome_permutation_odd_count(phrase_even_true)}")
    print(f"Palindrome Permutation Odd True: {is_palindrome_permutation_odd_count(palindrome_permutation_odd_true)}")
    print(f"Palindrome Permutation Non-Letter Odd True: "
          f"{is_palindrome_permutation_odd_count(palindrome_permutation_non_letter_odd_true)}")
    print(f"Palindrome Permutation Odd False: {is_palindrome_permutation_odd_count(palindrome_permutation_odd_false)}")
    print(f"Palindrome Permutation Non-Letter Odd False: "
          f"{is_palindrome_permutation_odd_count(palindrome_permutation_non_letter_odd_false)}")

    print(f"\nThe following strings test is_palindrome_permutation_bit_vector.")
    print(f"Palindrome Permutation Even True: {is_palindrome_permutation_bit_vector(phrase_even_true)}")
    print(f"Palindrome Permutation Odd True: {is_palindrome_permutation_bit_vector(palindrome_permutation_odd_true)}")
    print(f"Palindrome Permutation Non-Letter Odd True: "
          f"{is_palindrome_permutation_bit_vector(palindrome_permutation_non_letter_odd_true)}")
    print(f"Palindrome Permutation Odd False: {is_palindrome_permutation_bit_vector(palindrome_permutation_odd_false)}")
    print(f"Palindrome Permutation Non-Letter Odd False: " 
          f"{is_palindrome_permutation_bit_vector(palindrome_permutation_non_letter_odd_false)}")
