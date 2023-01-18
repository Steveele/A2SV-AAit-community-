class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq=collections.Counter(arr)
        occurance=sorted(freq.values(),reverse=True)
        length=len(arr)//2
        removed=0

        for i in occurance:
            if(length>0):
                length-=i
                removed+=1
        return removed
            

        
