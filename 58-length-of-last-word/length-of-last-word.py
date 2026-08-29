class Solution(object):
    def lengthOfLastWord(self, s):
        w=s.split()
        return len(w[len(w)-1])

        """
        :type s: str
        :rtype: int
        """
        