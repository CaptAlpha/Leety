class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = (n * (n + 1)) // 2
        leftSum = 0

        for i in range(1, n + 1):
            leftSum += i
            rightSum = totalSum - leftSum

            if leftSum - i == rightSum:
                return i

        return -1  # If no pivot integer exists