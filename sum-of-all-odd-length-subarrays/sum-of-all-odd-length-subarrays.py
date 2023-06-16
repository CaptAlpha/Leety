class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarray = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                subarray.append(arr[i:j])
        sumarray = 0        
        for i in subarray:
            if len(i)%2==1:
                sumarray+=sum(i)
        return sumarray