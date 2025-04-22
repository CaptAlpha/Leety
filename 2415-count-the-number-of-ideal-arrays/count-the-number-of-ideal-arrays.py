class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        main_dp = dict()

        def dp(cur_maximum , max_possibles):
            if (cur_maximum , max_possibles) in main_dp:
                return main_dp[(cur_maximum , max_possibles)]

            res = math.comb(n-1,max_possibles -1)
            nxt = cur_maximum + cur_maximum

            if max_possibles == n or nxt > maxValue:
                return res

            while nxt<=maxValue:
                res += dp(nxt , max_possibles + 1)
                nxt += cur_maximum

            main_dp[(cur_maximum, max_possibles)] = res
            return res

        return sum([dp(i,1) for i in range(1, maxValue + 1)]) % (10**9 + 7)