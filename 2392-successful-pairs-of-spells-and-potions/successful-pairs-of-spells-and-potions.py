class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for i in spells:
            # Binary Search
            start = 0
            end = len(potions)-1
            lowestIndex = -1
            while(start<=end):
                mid = (start+end)//2
            
                check = potions[mid]*i >= success

                if check:
                    lowestIndex = mid
                    end = mid - 1
                else:
                    start = mid + 1

             # If found, count how many potions are >= that index
            if lowestIndex != -1:
                res.append(len(potions) - lowestIndex)
            else:
                res.append(0)
        return res