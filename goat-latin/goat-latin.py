class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split()
        res  = ""
        root = "maa"
        vowels = "aeiouAEIOU"
        for i in range(len(s)):
            if s[i][0] not in vowels:
                newString = s[i][1:]
                newString += s[i][0]
            else:
                newString = s[i]
            a = 'a'*i
            newString += root + a

            res+=newString + " "
        

        return res[:-1]
