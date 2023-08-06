class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i, j in nums1:
            if i not in dic:
                dic[i] = j
            else:
                dic[i]+=j
        for i, j in nums2:
            if i not in dic:
                dic[i] = j
            else:
                dic[i]+=j
        ans = []
        li = list(dic.keys())
        li.sort()
        for i in li:
            ans.append([i, dic[i]])
        return ans