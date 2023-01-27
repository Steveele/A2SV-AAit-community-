class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for j in range(len(nums)):
            if (nums[j]==0):
                k-=1
            if k < 0:
                k += 1 - nums[left]
                left+= 1
        return j - left + 1