class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mySet, ans =  set(), ""

        for path in range(len(paths)):
            mySet.add(paths[path][0])
            
        for path in range(len(paths)):
            if paths[path][-1] not in mySet:        
                ans = paths[path][-1]
        return ans