import heapq  
class Solution:  
    def clearStars(self, s: str) -> str:  
        hp = []  
        n = len(s)  

        for i, x in enumerate(s):  
            if x == "*": 
                if hp:  
                    heapq.heappop(hp)  
            else:  
                heapq.heappush(hp, (x, n-i))  
        hp.sort(key = lambda x: x[1])  
        hp = [i[0] for i in hp][::-1]

        return "".join(hp)  