class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        count = []
        for i in range(len(words)):
            if x in words[i]:
                count.append(i)
        return count