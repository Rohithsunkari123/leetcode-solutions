class Solution(object):
    def replaceElements(self, arr):
        rmax=-1
        for i in range(len(arr)-1,-1,-1):
            newmax=max(rmax,arr[i])
            arr[i]=rmax
            rmax=newmax
        return arr