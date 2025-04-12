class Solution:
    def __init__(self):
        self.tens = [1] * 11
        self.zero = [0] * 10
        self.seen = set()
        self.n = 0

    def build_tens(self):
        for i in range(1, 11):
            self.tens[i] = self.tens[i - 1] * 10

    def pal(self, x: int, dz: int, k: int) -> List[int]:
        palindrome = x 
        temp = x

        if self.n & 1:
            middle_digit = x % 10
            temp //= 10
        else:
            middle_digit = 0
        second_half = 0
        while temp > 0:
            second_half = second_half * 10 + temp % 10
            temp //= 10
        if self.n & 1:
            palindrome = x // 10 * 10 + middle_digit
            palindrome = palindrome * self.tens[dz - 1] + second_half
        else:
            palindrome = x * self.tens[dz] + second_half
        
        if palindrome % k != 0:
            return self.zero
        
        freq = [0] * 10
        temp_x = x
        if self.n & 1:
            freq[temp_x % 10] += 1
            temp_x //= 10
        while temp_x > 0:
            digit = temp_x % 10
            freq[digit] += 2
            temp_x //= 10
        return freq

    def perm(self, freq: List[int]) -> int:
        d = sum(freq)
        ans = 1
        if freq[0] > 0:
            ans = math.comb(d - 1, freq[0])
            d -= freq[0]
        for i in range(1, 10):
            if freq[i] > 0:
                ans *= math.comb(d, freq[i])
                d -= freq[i]
        return ans

    def countGoodIntegers(self, n: int, k: int) -> int:
        self.n = n
        if n <= 2:
            return 9 // k  
        self.build_tens()
        h = (n + 1) // 2
        ans = 0
  
        for i in range(self.tens[h - 1], self.tens[h]):
            freq = self.pal(i, h, k)
            if freq != self.zero and tuple(freq) not in self.seen:
                ans += self.perm(freq)
                self.seen.add(tuple(freq))
        return ans