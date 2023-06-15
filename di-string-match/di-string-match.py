class Solution:
    def diStringMatch(self, s: str) -> List[int]:
#         A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
        res = []

        left = 0
        right = len(s)
        # if s[0] == 'D':
        #     res.append(right)
        #     right-=1
        # else:
        #     res.append(left)
        #     left += 1

        for i in s[:]:
            if i == 'D':
                res.append(right)
                right-=1
            else:
                res.append(left)
                left += 1
        res.append(right)
        return res


