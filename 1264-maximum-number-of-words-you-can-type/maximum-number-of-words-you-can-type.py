class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        li = text.split(" ")
        counter = 0
        arr = set()
        for i in brokenLetters:
            for j in li:
                if i in j:
                    arr.add(j)

        for i in li:
            if i not in arr:
                counter+=1
        return counter

                    
