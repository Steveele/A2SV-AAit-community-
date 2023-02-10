class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastI={}
        out=[]
        size,endI=0,0

        for i , c in enumerate(s):
            lastI[c]=i
        
        for i ,c in enumerate(s):
            size+=1
            endI=max(endI,lastI[c])
            if i==endI:
                out.append(size)
                size=0
        return out

       