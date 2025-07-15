class Solution:
    def isValid(self, word: str) -> bool:
        vowel = 0
        consonant = 0
        if len(word) <3 or word.isalnum() is False:
            print("Yes")
            return False
        vowels = ['a', 'e', 'i', 'o', 'u']

        for i in word:
            if i.isalpha():
                print(i, vowels)
                if i.lower() in vowels:
                    vowel+=1
                else:
                    consonant+=1
        print(vowel, consonant)
        if vowel > 0 and consonant > 0:
            return True
        print("last guy :|")
        return False
        