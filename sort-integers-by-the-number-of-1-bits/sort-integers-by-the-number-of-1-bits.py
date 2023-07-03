class Solution:
    def con(self, n, s= ""):
        if n < 1:
            return s[::-1]
        s += str(n%2)
        n//=2
        return self.con(n, s)
        
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        dic = {}

        ans = []

        for i in arr:
            count = self.con(i).count('1')
            if count not in dic:
                dic[count] = [i]
            else:
                dic[count].append(i)
        
        sorted_keys = list(dic.keys())
        sorted_keys.sort()
        for i in sorted_keys:
            array = dic[i]
            array.sort()
            ans.extend(array)


        return ans
