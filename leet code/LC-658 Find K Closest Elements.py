class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        ind = bisect_left(arr, x)

        l = ind - 1
        r = ind

        while k>0:
            if l<0:
                r+=1
            elif r>=n:
                l-=1
            elif abs(arr[l]-x) <= abs(arr[r]-x):
                l-=1
            else:
                r+=1
            k-=1
        return arr[l+1:r]