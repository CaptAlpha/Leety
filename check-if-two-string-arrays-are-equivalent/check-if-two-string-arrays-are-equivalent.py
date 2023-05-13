class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1, s2 = "",""

        if word1 == word2:
            return True
        
        if word1 is None or word2 is None:
            return False

        for i in word1:
            s1+=i
        for i in word2:
            s2+=i

        return s1==s2