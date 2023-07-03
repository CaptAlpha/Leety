class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        transfers = [0]*n
        self.ans = 0
        def backtrack(ind, count, transfers):
            if ind == len(requests):
                if transfers == [0]*n:
                    self.ans = max(self.ans, count)
                return

            backtrack(ind+1, count, transfers)

            transfers[requests[ind][0]]-=1
            transfers[requests[ind][1]]+=1

            backtrack(ind+1, count+1, transfers)

            transfers[requests[ind][0]]+=1
            transfers[requests[ind][1]]-=1

        backtrack(0,0,transfers)

        return self.ans
                    
        