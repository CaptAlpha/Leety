class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dic = {}
        for i in list(set(nums1)):
            if i not in dic:
                dic[i] = [1, 0, 0]
        for i in list(set(nums2)):
            if i not in dic:
                dic[i] = [0, 1, 0]
            else:
                dic[i] = [1,1,0]
        for i in list(set(nums3)):
            if i not in dic:
                dic[i] = [0, 0, 1]
            else:
                dic[i] = [1, 1, 1]
        arr = []
        for i, j in dic.items():
            if sum(j) >= 2:
                arr.append(i)
        return arr
