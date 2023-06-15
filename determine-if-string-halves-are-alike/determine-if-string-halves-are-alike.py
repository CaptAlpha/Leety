class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # You are given a string s of even length. 

        # Split this string into two halves of equal lengths, 
        n = len(s)//2
        # and let a be the first half and b be the second half.
        a = s[:n]
        b= s[n:]
        # Two strings are alike if they have the same number of vowels
        flag = False
        vowel= "aeiouAEIOU"
        cA, cB = 0, 0
        for i in a:
            if i in vowel:
                cA+=1
        for i in b:
            if i in vowel:
                cB+=1
        # Return true if a and b are alike. Otherwise, return false.
        return cA==cB