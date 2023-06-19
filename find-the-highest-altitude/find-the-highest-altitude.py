class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        runningSum = 0
        maxAltitude = 0
        for i in gain:
            runningSum += i
            maxAltitude = max(runningSum, maxAltitude)
        return maxAltitude