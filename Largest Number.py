class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort()
        answer=[]
        count=0
        for i in range(len(nums)):
            nums[i]=str(nums[i])
            if nums[i]=="0":
                 count+=1
            if (count>=len(nums)):
                return "0"


           
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                
                if (nums[j]+nums[j+1]<nums[j+1]+nums[j]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                else:
                    continue
        for i in nums:
             answer=''.join(nums)


        return answer