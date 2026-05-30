class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #instead of normal apporach we are going to use binary search
        l=0
        r=len(nums)-1


        while l<r:
            mid=(l+r)//2

            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid
        return l
        '''
        n=len(nums)
        nums=[float('-inf')]+nums+[float('-inf')]

        max_val=float('-inf')
        ind=0
        for i in range(1,n+1):
            if nums[i-1]<nums[i]>nums[i+1]:
                if nums[i]>max_val:
                    max_val=nums[i]
                    ind=i
        return ind-1'''

        