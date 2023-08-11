class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        a = []
        for i in strs:
            if i.isnumeric():
                a.append(int(i))
            else:
                a.append(len(i))
        return max(a)