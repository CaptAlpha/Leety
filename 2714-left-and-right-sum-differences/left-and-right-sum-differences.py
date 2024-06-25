class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftArray = [0]
        leftArr = rightArr = []
        leftArray.extend(nums[:len(nums)-1])
        leftSum = 0
        print(leftArray)
        for i in leftArray:
        
            leftSum+=i
            leftArr.append(leftSum)


        nums = nums[::-1]
        rightArray = [0]
        rightArray.extend(nums[:len(nums)-1])
        print(rightArray)


        rightSum = 0

        for i in rightArray:
            rightSum+=i
            rightArr.append(rightSum)

        ans = []

        rightArr = rightArr[::-1]

        print(rightArr)


        for i in range(len(leftArray)):
            ans.append(abs(leftArr[i]-rightArr[i]))
        return ans
