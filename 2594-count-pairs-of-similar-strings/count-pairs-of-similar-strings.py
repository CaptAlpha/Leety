class Solution:
    def similarPairs(self, words):
        def get_unique_chars(word):
            return ''.join(sorted(set(word)))

        char_count = defaultdict(int)
        for word in words:
            unique_chars = get_unique_chars(word)
            char_count[unique_chars] += 1

        counter = 0
        for count in char_count.values():
            counter += count * (count - 1) // 2

        return counter
