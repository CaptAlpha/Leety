class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        checkSet = set()
        for r in range(len(s)):
            while(s[r] in checkSet):
                checkSet.remove(s[l])
                l+=1
            w = (r-l)+1
            checkSet.add(s[r])
            longest = max(longest,w)
        return longest
