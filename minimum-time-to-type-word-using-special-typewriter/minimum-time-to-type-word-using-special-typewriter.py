class Solution:
    def minTimeToType(self, word: str) -> int:
        counter=len(word)
        dic={}
        a = 97
        for i in range(1, 27):
            if i not in dic: dic[chr(i+96)] = i

        print(dic) 

        prev = 'a'
        for i in word:
            time = abs(dic[i] - dic[prev])%26 
            print(i, prev, time)
            prev = i
            
            counter+=min(time, 26-time)
        return counter
