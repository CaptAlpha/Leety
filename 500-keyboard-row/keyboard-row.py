class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        ref = [ "qwertyuiop","asdfghjkl","zxcvbnm"]
        

        def checkIfSameRow(w, ref):
            firstChar = w[0]
            rowNum = 0
            for row in range(len(ref)):
                if firstChar.lower() in ref[row]:
                    rowNum = row
            for nextChar in w[:]:
                for row in range(len(ref)):
                    if nextChar.lower() in ref[row]:
                        if row != rowNum:
                            return False
            return True
        ans  = []
        for w in words:
            if checkIfSameRow(w, ref):
                ans.append(w)
        return ans
                
        

