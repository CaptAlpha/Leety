class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(i) for i in digits)
        n = int(s)+1
        s = str(n)
        ans = []
        for i in s:
            ans.append(int(i))


        return ans