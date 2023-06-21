class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashm:
                return [hashm[difference], i]
            hashm[num] = i
        return []'__main__':