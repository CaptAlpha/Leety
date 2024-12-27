class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = [1]*len(nums)
        postfixArray = [1]*len(nums)
        for i in range(1, len(nums)):
            prefixArray[i] =prefixArray[i-1]*nums[i-1]

        nums = nums[::-1]
        for i in range(1, len(nums)):
            postfixArray[i] = postfixArray[i-1]*nums[i-1]
        ans = []
        postfixArray = postfixArray[::-1]
        print(postfixArray)
        for i in range(len(nums)):
            ans.append(prefixArray[i]*postfixArray[i])
        return ans