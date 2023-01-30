class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
       right=len(nums)-2

       while right>=0 and nums[right]>=nums[right+1]:
           right-=1
        
       if right<0:
            nums=nums.sort()
       else:
            for i in reversed(range(right,len(nums))):
                if nums[i]>nums[right]:
                    nums[i],nums[right]=nums[right],nums[i];
                    break
            nums[right+1:]=reversed(nums[right+1:])
