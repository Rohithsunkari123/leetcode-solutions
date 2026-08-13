class Solution(object):
    def validPalindrome(self, s):
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skpl,skpr=s[l+1:r+1],s[l:r]
                return skpl==skpl[::-1] or skpr==skpr[::-1]
            l+=1
            r-=1
        return True
            

        