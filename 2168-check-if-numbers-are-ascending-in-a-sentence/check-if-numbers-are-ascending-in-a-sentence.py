class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(" ")
        prev = 0
        for i in s:
            if i.isnumeric():
                print(prev, int(i))
                if prev!=-1 and prev < int(i):
                    prev = int(i)
                else:
                    return False
        return True
