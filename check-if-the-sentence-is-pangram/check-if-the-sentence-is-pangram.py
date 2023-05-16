class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = {}
        for i in range(65, 91):
            dic[chr(i)] = 0
        
        for i in sentence:
            if i.upper() in dic:
                dic[i.upper()] += 1
        print(dic)
        for i in dic.values():
            if(i == 0):
                return False
        return True

        