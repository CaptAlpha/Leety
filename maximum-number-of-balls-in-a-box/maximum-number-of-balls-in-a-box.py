class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        n = highLimit - lowLimit + 1
        arr = [0]*(highLimit+1)

        for i in range(lowLimit,highLimit+1):
            s = list(str(i))
            m = 0
            for k in s:
                m+=int(k)
            arr[m]+=1
        return max(arr)
