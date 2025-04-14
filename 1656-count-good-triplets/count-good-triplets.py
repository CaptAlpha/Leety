class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:

        ans = 0

        for num1, num2, num3 in combinations(arr, 3):

            if (abs(num1-num2) <= a and 
                abs(num2-num3) <= b and 
                abs(num1-num3) <= c):  ans+= 1
          
        return ans