class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        common_chars = list(words[0])

        for i in range(1, len(words)):
            temp_chars = ""
            t = words[i]

            for char in common_chars:
                if char in t:
                    temp_chars += char
                    t = t.replace(char, '', 1)  # Remove the used character from t

            common_chars = temp_chars

        return common_chars