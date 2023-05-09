class Solution:

    def pow(self, x, n):

        if(n==0):
            return 1
        if(x==0):
            return 0

        return x*self.pow(x,n-1)
        


    def myPow(self, x: float, n: int) -> float:

        isPositive = 1
        if(n<0):
            isPositive = 0
        n = abs(n)
        try:
            if(isPositive):
                return pow(x, n)
            else:
                return float(1/pow(x, n))
        except:
            return 0.00000
            
        
        
        

    
        
