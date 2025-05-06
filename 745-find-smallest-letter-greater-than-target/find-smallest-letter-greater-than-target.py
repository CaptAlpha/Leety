class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        start = 0
        end = len(letters) - 1

        res = -1

        while(start <= end):
            mid = (start+end)//2

            if target < letters[mid]:
                end = mid - 1
            else:
                res = mid
                start = mid + 1
        
        if res == -1: return letters[0]

        print(res+1)
        index = (res+1)%len(letters)
        print(index)
        return letters[start%(len(letters))]