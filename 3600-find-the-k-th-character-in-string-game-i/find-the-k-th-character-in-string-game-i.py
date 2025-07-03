class Solution:
    def kthCharacter(self, k: int) -> str:
        res='a'
        flag=True
        while flag:
            word=''
            for i in range(len(res)):
                if res[i]=='z':
                    word+='a'
                else:
                    new=ord(res[i])+1
                    word+=chr(new)
            res+=word
            if (len(res)>=k):
                flag=False
        return res[k-1]
        