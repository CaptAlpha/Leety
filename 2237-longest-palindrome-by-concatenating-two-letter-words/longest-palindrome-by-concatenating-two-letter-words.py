from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        length = 0
        middle_used = False
        
        # Process same-letter words
        same_letter_pairs = 0
        for word in word_count:
            if word[0] == word[1]:
                count = word_count[word]
                pairs = count // 2
                same_letter_pairs += pairs
                if count % 2 == 1 and not middle_used:
                    middle_used = True
        
        length += same_letter_pairs * 4
        if middle_used:
            length += 2
        
        # Process different-letter words
        processed = set()
        for word in word_count:
            if word[0] != word[1] and word not in processed:
                reversed_word = word[::-1]
                if reversed_word in word_count:
                    min_pairs = min(word_count[word], word_count[reversed_word])
                    length += min_pairs * 4
                    processed.add(word)
                    processed.add(reversed_word)
        
        return length