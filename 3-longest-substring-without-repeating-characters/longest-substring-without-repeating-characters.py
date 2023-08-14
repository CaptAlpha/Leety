class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # To store the index of the last occurrence of each character
        start = 0            # Start of the sliding window
        max_length = 0       # Maximum length of substring without repeating characters

        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1

            char_index_map[char] = end
            max_length = max(max_length, end - start + 1)

        return max_length
