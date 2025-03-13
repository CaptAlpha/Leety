class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h1 = Counter(ransomNote)
        h2 = Counter(magazine)

        print(h1, h2)
        for i in h1.keys():
            if i not in magazine or h1[i] > h2[i]:
                print(h1[i])
                return False
        
        return True