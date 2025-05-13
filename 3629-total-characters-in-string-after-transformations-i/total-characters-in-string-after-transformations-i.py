class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c)-ord('a')] += 1

        for _ in range(t):
            cnt = [cnt[-1]] + cnt[:-1]
            cnt[1] += cnt[0]

        return sum(cnt) % (10**9+7)