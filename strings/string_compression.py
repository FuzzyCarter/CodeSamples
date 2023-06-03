"""
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string
aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your
method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Solution 1: Concatenation
Solution 2: StringBuilder
Solution 3: Count Occurrences First

Author: Fuzzy Carter
"""

from function_timer import function_timer


@function_timer
def compress_concatenation(uncompressed: str) -> str:
    """
    Compress the string by concatenating the characters and their counts.

    Iterate through the string and count the number of consecutive characters. If the next character is different from
    the current character, append the current character and its count to the result string. Reset the count to 0. If the
    compressed string is not shorter than the original string, return the original string.

    Time Complexity: O(p + k^2), where p is the size of the original string and k is the number of character sequences.
    Space Complexity: O(p)
    """
    compressed = ""
    count_consecutive = 0
    for i in range(len(uncompressed)):
        count_consecutive += 1

        # If next character is different from current, append this char to result
        if i + 1 >= len(uncompressed) or uncompressed[i] != uncompressed[i + 1]:
            compressed += uncompressed[i] + str(count_consecutive)
            count_consecutive = 0

    return compressed if len(compressed) < len(uncompressed) else uncompressed


@function_timer
def compress_string_builder(uncompressed: str) -> str:
    """
    String builder solution to compress the string by adding the characters and their counts to a string builder.

    Iterate through the string and count the number of consecutive characters. If the next character is different from
    the current character, append the current character and its count to the result list. If the compressed string is
    not shorter than the original string, return the original string.

    Time Complexity: O(p + k^2), where p is the size of the original string and k is the number of character sequences.
    Space Complexity: O(p)

    This solution is marginally better than compress_concatenation because it avoids the string concatenation problem
    by building a list of characters and then joining them at the end of the function. However, this solution is still
    O(p + k^2) because string concatenation is still O(p + k^2).
    """
    compressed = []
    count_consecutive = 0
    for i in range(len(uncompressed)):
        count_consecutive += 1

        # If next character is different from current, append this char to result
        if i + 1 >= len(uncompressed) or uncompressed[i] != uncompressed[i + 1]:
            compressed.append(uncompressed[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0

    return "".join(compressed) if len(compressed) < len(uncompressed) else uncompressed


@function_timer
def compress_count_occurrences(uncompressed: str) -> str:
    """
    Count the number of occurrences of each character in the uncompressed string. If the compressed string is not
    shorter than the original string, return the original string.

    Time Complexity: O(p + k^2), where p is the size of the original string and k is the number of character sequences.
    Space Complexity: O(p)

    This solution is faster only if the compressed string is longer than the original string. If the compressed string
    is longer than the original string, then the string builder solution is faster.
    """

    # Check if compression would create a longer string
    final_length = count_occurrences(uncompressed)
    if final_length >= len(uncompressed):
        return uncompressed

    compressed = []
    count_consecutive = 0
    for i in range(len(uncompressed)):
        count_consecutive += 1

        # If next character is different from current, append this char to result
        if i + 1 >= len(uncompressed) or uncompressed[i] != uncompressed[i + 1]:
            compressed.append(uncompressed[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0

    return "".join(compressed)


# -- Helper Functions --------------------------------------------------------
def count_occurrences(uncompressed: str) -> int:
    """
    Count the number of occurrences of each character in the uncompressed string by iterating through the string and
    counting the number of consecutive characters. If the next character is different from the current character,
    increment the compressed length by 1 + the length of the count of consecutive characters.
    """
    compressed_length = 0
    count_consecutive = 0
    for i in range(len(uncompressed)):
        count_consecutive += 1

        # If next character is different from current, append this char to result
        if i + 1 >= len(uncompressed) or uncompressed[i] != uncompressed[i + 1]:
            compressed_length += 1 + len(str(count_consecutive))
            count_consecutive = 0

    return compressed_length


if __name__ == "__main__":
    compressible = "aabcccccaaa"
    compressible_original_shorter = "aabbccdd"
    compressible_long = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzzzzzzzzzzzzzzz"
    compressible_boundary = "aabbccddeeffgghhiijjkkllmmnnoooooooooooooooooooooooppqqrrssttuuvvwwxxyyzzAABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"

    incompressible = "abcdefg"
    incompressible_long = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr"

    print(f"Concatentation Tests:")
    print(f"Compressible: {compressible} -> {compress_concatenation(compressible)}")
    print(f"Compressible, Original Shorter: {compressible_original_shorter} -> "
          f"{compress_concatenation(compressible_original_shorter)}")
    print(f"Compressible Long: {compressible_long} -> {compress_concatenation(compressible_long)}")
    print(f"Compressible Boundary: {compressible_boundary} -> {compress_concatenation(compressible_boundary)}")
    print(f"Incompressible: {incompressible} -> {compress_concatenation(incompressible)}")
    print(f"Incompressible Long: {incompressible_long} -> {compress_concatenation(incompressible_long)}")

    print(f"\nString Builder Tests:")
    print(f"Compressible: {compressible} -> {compress_string_builder(compressible)}")
    print(f"Compressible, Original Shorter: {compressible_original_shorter} -> "
          f"{compress_string_builder(compressible_original_shorter)}")
    print(f"Compressible Long: {compressible_long} -> {compress_string_builder(compressible_long)}")
    print(f"Compressible Boundary: {compressible_boundary} -> {compress_string_builder(compressible_boundary)}")
    print(f"Incompressible: {incompressible} -> {compress_string_builder(incompressible)}")
    print(f"Incompressible Long: {incompressible_long} -> {compress_string_builder(incompressible_long)}")

    print(f"\nCount Occurrences Tests:")
    print(f"Compressible: {compressible} -> {compress_count_occurrences(compressible)}")
    print(f"Compressible, Original Shorter: {compressible_original_shorter} -> "
          f"{compress_count_occurrences(compressible_original_shorter)}")
    print(f"Compressible Long: {compressible_long} -> {compress_count_occurrences(compressible_long)}")
    print(f"Compressible Boundary: {compressible_boundary} -> {compress_count_occurrences(compressible_boundary)}")
    print(f"Incompressible: {incompressible} -> {compress_count_occurrences(incompressible)}")
    print(f"Incompressible Long: {incompressible_long} -> {compress_count_occurrences(incompressible_long)}")


