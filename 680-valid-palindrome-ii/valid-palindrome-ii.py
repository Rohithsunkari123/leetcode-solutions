class Solution(object):
    def validPalindrome(self, s):
        l=0
        r=len(s)-1
        while l < r:
            if s[l]!=s[r]:
                sl=s[l+1:r+1]
                sr=s[l:r]
                return sl == sl[::-1] or sr==sr[::-1]
            l+=1
            r-=1
        return True
            


       
            

        