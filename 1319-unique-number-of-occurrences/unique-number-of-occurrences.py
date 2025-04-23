class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        def count(i):
            return arr.count(i)
        s = []
        for i in list(set(arr)):
            if count(i) in s:
                print(count(i), s)
                return False
            x = count(i)
            s.append(x)
            # print(i, s)
        return True