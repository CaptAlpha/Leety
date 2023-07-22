class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l=r=m=0
        for i in range(len(s)):
            if s[i]=='(':
                l+=1
            else:
                r+=1
            if l==r: #for balanced parantheses
                m=max(m,l+r)
            elif r>l: #invalid case
                l=r=0
        l=r=0
# We are traversing right to left for the test case where opening brackets are more than closing brackets. eg: s = "(()"
        for i in range(len(s)-1,-1,-1):
            if s[i]=='(':
                l+=1
            else:
                r+=1
            if l==r: #for balanced parantheses
                m=max(m,l+r)
            elif l>r: #invalid case
                l=r=0  
        return m