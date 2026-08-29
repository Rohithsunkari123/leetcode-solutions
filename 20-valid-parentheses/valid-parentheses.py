class Solution(object):
    def isValid(self, s):
        b={']':'[',')':'(','}':'{'}
        st=[]
        for i in s:
            if i in b:
                if st and b[i]==st[-1]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return not st



        """
        :type s: str
        :rtype: bool
        """
        