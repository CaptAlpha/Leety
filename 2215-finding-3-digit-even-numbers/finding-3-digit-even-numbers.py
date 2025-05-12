class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()  # Use a set to avoid duplicates
        
        def backtrack(temp, used):
            if len(temp) == 3:
                num = temp[0]*100 + temp[1]*10 + temp[2]
                if num % 2 == 0 and num >= 100:
                    res.add(num)
                return
            
            for i in range(len(digits)):
                if not used[i]:
                    # Skip leading zeros
                    if len(temp) == 0 and digits[i] == 0:
                        continue
                    used[i] = True
                    backtrack(temp + [digits[i]], used)
                    used[i] = False
        
        backtrack([], [False]*len(digits))
        return sorted(res)