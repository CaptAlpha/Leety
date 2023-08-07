class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        counter=0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] == words[j][::-1] and i != j:
                    counter+=1
        return counter