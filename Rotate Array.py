class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        r=[0]*len(nums)
        for i in range(len(nums)):
            n=len(nums)-1
            if n>=k+i:
                r[i+k]=nums[i]
            else:
                r[(i+k)%len(nums)]=nums[i]
        for i in range(len(nums)):
            nums[i]=r[i]


              
