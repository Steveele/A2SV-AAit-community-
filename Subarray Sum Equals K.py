class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       result=0
       current_sum=0
       sum={0:1}

       for i in nums:
           current_sum+=i
           difference=current_sum-k

           result+=sum.get(difference,0)
           sum[current_sum]=1+sum.get(current_sum,0)
       
       return result