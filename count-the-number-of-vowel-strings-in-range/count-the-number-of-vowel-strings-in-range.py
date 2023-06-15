class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        counter=0
        vowels="aeiou"
        for i in range(left, right+1):
            word = words[i]
            if word[-1]  in vowels:
                if word[0]  in vowels:
                    counter+=1
        return counter