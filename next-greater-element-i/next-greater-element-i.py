class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(lambda: -1)
        for i in range(0, len(nums2)-1):
            for j in range(i+1, len(nums2)):
                if nums2[i] < nums2[j]:
                    dic[nums2[i]] = nums2[j]
                    break
            
        ans = []

        for i in nums1:
            ans.append(dic[i])

        return ans