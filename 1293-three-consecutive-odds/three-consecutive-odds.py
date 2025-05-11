class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = j = 0
        flag = False
        count = 0
        # while(j < len(arr)):
        #     if arr[j]%2 == 1:
        #         count+=1

        #     if j - i + 1 < 3:
        #         j+=1
            
        #     elif j - i + 1 == 3:
        #         if count == 3:
        #             return True

        while(j < len(arr)):
            if arr[j]%2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
                i+=1
            j+=1
        return False
        
                

            