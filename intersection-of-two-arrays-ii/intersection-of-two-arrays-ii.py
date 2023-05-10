class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute Force Approach
        li = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i]==nums2[j]):
                    li.append(nums1[i])

        li = list(set(li))
        dic = {}
        for i in nums1:
            if(i not in dic):
                dic[i] = 1
            else:
                dic[i]+=1

        for i in nums2:
            if i in dic:
                dic[i] = min(dic[i], nums2.count(i))

        ans = []

        for x, y in dic.items():
            if x in li:
                for j in range(y):
                    ans.append(x)

        return ans

            

