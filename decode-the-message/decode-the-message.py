class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a = 97
        z = a+97
        dic = {}
        s = ""
        key2 = key.split(" ")
        for i in key2:
            s+=i
        for i in s:
            if i not in dic:
                dic[i] = chr(a)
                a+=1
        res = ""
        for i in message:
            if i == " ":
                res+=" "
            else:
                res+=dic[i]
        

        return res
