class Solution:
    def isPal(self, num: int, base: int) -> bool:
        digits = []
        while num:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]

    def kMirror(self, k: int, n: int) -> int:
        cnt = 0
        total_sum = 0

        # 1-digit numbers
        for i in range(1, 10):
            if self.isPal(i, k):
                total_sum += i
                cnt += 1
                if cnt == n:
                    return total_sum

        length = 1
        while cnt < n:
            start = 10**(length - 1)
            end = 10**length

            # Even-length palindromes
            for i in range(start, end):
                num = str(i)
                pal_str = num + num[::-1]
                pal = int(pal_str)
                if self.isPal(pal, k):
                    cnt += 1
                    total_sum += pal
                    if cnt == n:
                        return total_sum

            # Odd-length palindromes
            for i in range(start, end):
                num = str(i)
                for mid in range(10):
                    pal_str = num + str(mid) + num[::-1]
                    pal = int(pal_str)
                    if self.isPal(pal, k):
                        cnt += 1
                        total_sum += pal
                        if cnt == n:
                            return total_sum

            length += 1

        return total_sum