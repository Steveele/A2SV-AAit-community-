class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        r=0
        l=0
        ans=0
       
        
      

        for i in range(1,len(arr)-1):
            if (arr[i]>arr[i-1] and arr[i]>arr[i+1]):
                l=i
                r=i
                counter=1
                while (l>0 and arr[l]>arr[l-1]):
                    counter+=1
                    l-=1
                ans=max(ans,counter)
                while (r<len(arr)-1 and arr[r]>arr[r+1]):
                    r+=1
                    counter+=1
                ans=max(ans,counter)
        return ans
        