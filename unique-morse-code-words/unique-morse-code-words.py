class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alph = []
        for i in range(65, 91):
            alph.append(chr(i).lower())
        ans = []

        for i in words:
            s  = ""
            for j in i:
                l = alph.index(j)
                s+=morse[l]
            ans.append(s)

        return len(set(ans))    

        
