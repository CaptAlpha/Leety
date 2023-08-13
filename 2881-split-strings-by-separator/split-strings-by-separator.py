class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for i in words:
            s = i.split(separator)
            ans.extend(s)
        return [i for i in ans if i!=""]
