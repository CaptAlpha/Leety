class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = Counter(s)
        print(hashmap)
        c = s.count(s[0])
        for i in hashmap.values():
            if i!=c:
                return False
        return True