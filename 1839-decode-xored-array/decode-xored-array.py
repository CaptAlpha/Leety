class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # def xor(a, b):
        #     return 
        ans = [first]
        for i in encoded:
            ans.append(i^ans[-1])
        return ans