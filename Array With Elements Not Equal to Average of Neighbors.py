class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)-1):
                if (nums[j]==(nums[j-1] + nums[j+1]) / 2):
                    
                    nums[j] , nums[j+1]=nums[j+1] ,nums[j]
        return nums
            
         