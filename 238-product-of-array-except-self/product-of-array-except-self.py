class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [1]
        rightProduct = [1]

        for i in nums[:-1]:
            p = i*leftProduct[-1]
            leftProduct.append(p)

        nums = nums[::-1]

        for i in nums[:-1]:
            p = i*rightProduct[-1]
            rightProduct.append(p)
        

        rightProduct = rightProduct[::-1]

        ans = []
        for i in range(len(nums)):
            ans.append(leftProduct[i]*rightProduct[i])
        
        return ans
        
