class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        counter=0
        arr = []
        for i in range(1, a+1):
            if a%i==0:
                arr.append(i)
        for i in range(1, b+1):
            if b%i==0:
                if i in arr:
                    print(i)
                    counter+=1
        return counter
        