class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        si=0
        li=0
        st=set()
        res=0
        while li< len(s):
            if s[li] in st:
                st.remove(s[si])
                si+=1
            else:
                st.add(s[li])
                res=max(res,li-si+1)
                li+=1
        return res
        