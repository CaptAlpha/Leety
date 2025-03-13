class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        def isLost(dist):
            for i in dist:
                if i == 0:
                    return True
            return False

        time = [0]*len(dist)
        for i in range(len(dist)):
            time[i] = math.ceil(dist[i] / speed[i])
        
        time.sort()
        print(time)
        ans = 1

        for i in range(1,len(time)):
            if time[i] > i:
                ans+=1
            else: 
                break

                
                
        
        return ans