class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        flowerbed = flowerbed[::-1]
        flowerbed.append(0)
        flowerbed = flowerbed[::-1]

        for i in range(1,len(flowerbed)-1):

            
            if n == 0:
                return True
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n-=1
            if n == 0:
                return True

        return False
            



            
