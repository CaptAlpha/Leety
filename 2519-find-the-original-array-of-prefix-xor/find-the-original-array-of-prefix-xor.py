class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res= [0 for _ in range(len(pref))]

        res[0] = pref[0]

        for i in range(1, len(pref)):
            res[i] = pref[i-1]^pref[i]

        return res