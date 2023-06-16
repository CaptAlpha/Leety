class Solution:
    def numberOfMatches(self, n: int) -> int:
        counter=0
        rounds = 0
        advance = n

        while(n>1):
            rounds += 1
            if n%2 == 0:
                counter+=n//2
                n//=2
            else:
                counter += (n - 1) // 2
                n=((n - 1) // 2) + 1
            print("Rounds = ", rounds, "n = ", n, "counter = ", counter)
        return counter
        

