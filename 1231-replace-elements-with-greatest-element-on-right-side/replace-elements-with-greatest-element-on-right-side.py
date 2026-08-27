class Solution(object):
    def replaceElements(self, arr):
        rm=-1
        for i in range(len(arr)-1,-1,-1):
            newmax=max(rm,arr[i])
            arr[i]=rm
            rm=newmax
        return arr