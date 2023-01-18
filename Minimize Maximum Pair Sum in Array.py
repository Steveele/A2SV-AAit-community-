class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        sums=0
        while(l<r):
            sums= max(sums,nums[l]+nums[r])
            l+=1
            r-=1
        return sums