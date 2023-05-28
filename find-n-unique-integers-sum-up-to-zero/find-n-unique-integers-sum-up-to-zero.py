class Solution:
    def sumZero(self, n: int) -> List[int]:
        li = []
        for i in range(1,n):
            li.append(i)

        li.append(-1*(sum(li)))

        return li