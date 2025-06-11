class Solution:

    def maxDifference(self, s: str, k: int, mxDiff = -inf) -> int:

        for a, b in permutations('01234', 2):
            if not(a in s and b in s): continue

            prefs = list(zip(accumulate([(ch == a) for ch in s], initial = 0),
                             accumulate([(ch == b) for ch in s], initial = 0)))
            
            diff = {(0, 0): inf, (0, 1): inf, (1, 0): inf, (1, 1): inf}
            i, aLeft, bLeft = 0, 0, 0

            for j, (aRght, bRght) in enumerate(prefs[k:]):

                while i <= j and aRght > aLeft and bRght > bLeft:
                    parity = (aLeft %2, bLeft %2)
                    diff[parity] = min(diff[parity],  aLeft - bLeft)
                    i += 1
                    aLeft, bLeft = prefs[i]

                parity = (1 - aRght %2, bRght %2)
                mxDiff = max(mxDiff, aRght - bRght - diff[parity])

        return mxDiff