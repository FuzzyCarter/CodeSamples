"""
Given a string, write a function to check if it is a permutation of a palindrome.

A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

You can ignore casing and non-letter characters.

Example: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)

HINT: You do not have to-and should not-generate all permutations. This would be very inefficient.
HINT: What characteristics would a string that is a permutation of a palindrome have?
HINT: Have you tried a hash table? You should be able to get this down to O(N) time.
HINT: Can you reduce the space using a bit vector?

Author: Fuzzy Carter
"""

from string import ascii_lowercase
from typing import Dict
from function_timer import function_timer


@function_timer
def is_palindrome_permutation_hash_table(palindrome_permutation: str) -> bool:
    """
    Check if is palindrome permutation by using a hash table to count the number of times each character appears in the
    string. Then, iterate through the hash table and count the number of characters that appear an odd number of times.
    If more than one character appears an odd number of times, return False.

    Time Complexity: O(n)
    Space Complexity: O(n)
    
    :param palindrome_permutation: The potential palindrome permutation.
    :return: True if the string is a palindrome permutation.
    """

    character_count = get_char_frequency(palindrome_permutation)
    return check_max_one_odd_character(character_count)


# -- Helper Functions ---------------------------------------------------------

def get_char_frequency(palindrome_permutation: str) -> dict:
    """
    Get the frequency of each character in the string.

    This function will not count non-letter characters and treat upper and lower case characters as the same.

    :param palindrome_permutation:
    :return: A dictionary containing the frequency of each character in the string.
    """
    character_count = {}

    for char in palindrome_permutation:
        char = char.lower()

        if char in ascii_lowercase: # Ignore non-letter characters.
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

if __name__ == "__main__":
    palindrome_permutation_even_true = "k a aky"
    palindrome_permutation_odd_true = "Tact Coa"
    palindrome_permutation_non_letter_odd_true = "$%^&*()_++Tact Coa!##  .,<>/?~`][}{]"

    palindrome_permutation_odd_false = "Tact Coaa"
    palindrome_permutation_non_letter_odd_false = "$%^&*()_++car!RaCee##  .,<>/?~`][}{]"

    print(f"Palindrome Permutation Even True: {is_palindrome_permutation_hash_table(palindrome_permutation_even_true)}")
    print(f"Palindrome Permutation Odd True: {is_palindrome_permutation_hash_table(palindrome_permutation_odd_true)}")
    print(f"Palindrome Permutation Non-Letter Odd True: "
          f"{is_palindrome_permutation_hash_table(palindrome_permutation_non_letter_odd_true)}")
    print(f"Palindrome Permutation Odd False: {is_palindrome_permutation_hash_table(palindrome_permutation_odd_false)}")
    print(f"Palindrome Permutation Non-Letter Odd False: "
          f"{is_palindrome_permutation_hash_table(palindrome_permutation_non_letter_odd_false)}")
