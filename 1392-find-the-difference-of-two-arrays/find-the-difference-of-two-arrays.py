class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # We need to find the whereabouts of each element in the arrays
        hashMap = {}
        arr1 = []
        arr2 = []

        for i in list(set(nums1)):
            hashMap[i] = [1, 0]
        for i in list(set(nums2)):
            if i not in hashMap:
                hashMap[i] = [0, 1]
            else:
                hashMap[i] = [1, 1]
    
        print(hashMap)

        for i, j in hashMap.items():
            if j == [0, 1]:
                arr2.append(i)
            elif j == [1, 0]:
                arr1.append(i)
        return [arr1, arr2]
        return [[]]
            