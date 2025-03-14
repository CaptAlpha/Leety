class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        hashmap = {}

        for i in nums1:
            if i not in hashmap:
                hashmap[i] = [1, 0 , 0]
        
        for i in nums2:
            if i not in hashmap:
                hashmap[i] = [0, 1 , 0]
            else:
                hashmap[i][1] = 1

        for i in nums3:
            if i not in hashmap:
                hashmap[i] = [0, 0 , 1]
            else:
                hashmap[i][2] = 1

        print(hashmap)
        ans = []
        for i, j in hashmap.items():
            if sum(j) >= 2:
                ans.append(i)
        return ans
        
