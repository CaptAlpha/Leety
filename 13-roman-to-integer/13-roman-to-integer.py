class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        """
        dic = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        su = 0
        li = []
        for i in range (0,len(s)-1):
            if dic[s[i]]<dic[s[i+1]]:
                su = su-dic[s[i]]
            else:
                su = su+dic[s[i]]
        su+=dic[s[-1]]
        return su
        