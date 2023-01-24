class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
  
        decq=collections.deque()
        incq=collections.deque()
        ans=0
        left=0
        for right,num in enumerate(nums):
            while decq and num > decq[-1]:
                decq.pop()
            decq.append(num)
            while incq and num < incq[-1]:
                incq.pop()
            incq.append(num) 
            while decq[0] - incq[0] > limit:
                if decq[0] == nums[left]:
                    decq.popleft()
                if incq[0]==nums[left]:
                    incq.popleft()
                left+=1
            ans=max(ans,right-left + 1)
        return ans
            