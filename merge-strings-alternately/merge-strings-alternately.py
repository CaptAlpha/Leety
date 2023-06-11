class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        diff = abs(len(word1) - len(word2))
        d=""
        for i in range(diff):
            d += "1"
        if len(word1)>=len(word2):
            word2 += d

        else:
            word1 += d
        s = ""
        print(word1, word2)
        for i in range(len(word2)):
            if word1[i] == "1":
                s+=""
            else:
                s+=word1[i]
            if word2[i] == "1":
                s+=""
            else:
                s+=word2[i]

        return s

                        

