class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
       
        leftsum=0

        for i in range(len(nums)):
            
            if(leftsum==sum(nums)-nums[i]-leftsum):
                return i
            leftsum+=nums[i]
        return -1