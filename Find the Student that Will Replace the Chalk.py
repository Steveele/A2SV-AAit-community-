class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sums=sum(chalk)
        k=k%sums
        i=0

        while(k>=0):
            if i < len(chalk):
                k-=chalk[i]
                i+=1
            
        return i-1


