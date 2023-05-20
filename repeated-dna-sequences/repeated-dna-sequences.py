class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashtable = {}
        if len(s) < 10:
            return []
        # if len(s) == 10:
        #     return [s]
        for i in range(len(s)-9):
            window = s[i:i+10]
            print(window)
            if window not in hashtable:
                hashtable[window] = 1
            else:
                hashtable[window] += 1

        ans = []
        for key, value in hashtable.items():
            if value>=2:
                ans.append(key)

        return ans



