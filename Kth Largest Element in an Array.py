class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        return nums[len(nums)-k]
