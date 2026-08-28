class Solution(object):
    def calPoints(self, operations):
        st=[]
        for i in operations:
            if i == "C" and st:
                st.pop()
            elif i == "D" and st:
                t=st[-1]
                st.append(2*t)
            elif i=="+":
                st.append(st[-1]+st[-2])
            else:
                st.append(int(i))
        return sum(st)

        """
        :type operations: List[str]
        :rtype: int
        """
        