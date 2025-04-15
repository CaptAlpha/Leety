class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        index={}
        r=0
        st=SortedList()
        for i,x in enumerate(nums1):
            index[x]=i
        for j,x in enumerate(nums2):
            i=index[x]
            st.add(i)
            left=st.index(i)
            right=(len(nums1)-1-i)-(j-left)
            r+=left*right
        return r
