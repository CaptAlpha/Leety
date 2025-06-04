class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        largest = max(word)
        res = largest

        if numFriends == 1:
            return word

        for i in range(n):
            if word[i] == largest:
                end = n - (numFriends - i)
                res = max(res, word[i:end+1])
        
        return res

            