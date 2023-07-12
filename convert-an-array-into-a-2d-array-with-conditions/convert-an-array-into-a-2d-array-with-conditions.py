class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        ans = []
        print(dic)
        for i in range(max(dic.values())):
            ans.append([])

        

        for i in range(max(dic.keys())+1):
            if i in dic:
                for j in range(dic[i]):
                    ans[j].append(i)

        return ans