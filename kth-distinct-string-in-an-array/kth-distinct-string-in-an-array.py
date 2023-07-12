class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {}

        ans = []

        for i in arr:
            if i  in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for i, j in dic.items():
            if j == 1:
                ans.append(i)

        if k > len(ans):
            return ""
        
        return ans[k-1]

        
