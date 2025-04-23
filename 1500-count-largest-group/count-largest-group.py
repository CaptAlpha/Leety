class Solution:
    def countLargestGroup(self, n: int) -> int:
        def calc(n):
            c = 0
            for i in str(n):
                c+=int(i)
            return c
        
        d = {}
        for i in range(1, n+1):
            # print(i)
            z = calc(i)
            if z not in d:
                d[z] = 1
            else:
                d[z]+=1
        count = 0
        print(d)
        p = max(list(d.values()))
        for i in d.values():
            print(i, p)
            if i == p:
                count+=1
        return count