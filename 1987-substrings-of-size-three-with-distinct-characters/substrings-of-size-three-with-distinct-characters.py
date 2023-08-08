class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        def goodString(s):
            dic = {}
            for i in s:
                if i not in dic:
                    dic[i] = 1
                else:
                    return False
            print(s)
            return True

        counter =0 

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if goodString(s[i:j]) and len(s[i:j]) == 3:
                    counter+=1
        return counter
