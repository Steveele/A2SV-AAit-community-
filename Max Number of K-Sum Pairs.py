class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0;
        L,R=0,len(nums)-1
        while(L<R):
            if (nums[L]+nums[R]<k):
                L+=1
            elif(nums[L]+nums[R]>k):
                R-=1
            else:
                count+=1
                L+=1
                R-=1
        return count


        