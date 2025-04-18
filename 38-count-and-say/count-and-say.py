class Solution:
    def countAndSay(self, n: int) -> str:

        def RLE(p):
            count = 1
            s = ""
            for i in range(0, len(p)-1):
                if p[i] == p[i+1]:
                    count+=1
                else:
                    s+=str(count) + p[i]
                    count = 1
       
            s+=str(count) + p[len(p)-1]
            return s

        print(RLE("1222")) # 111211
        # if n == 1:
        #     return "1"
        # return RLE(n-1)
        s = "1"
        for i in range(n-1):
            s = RLE(s)
        return s
    
