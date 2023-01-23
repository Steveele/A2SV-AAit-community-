class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dicti=collections.Counter(tasks)
        out=0
        numberofMax=0
       
       
        
        max_frequency=max(dicti.values())
        for i in dicti.values():
            if i==max_frequency:
                numberofMax+=1
        
        out=(max_frequency-1)*(n+1)+ numberofMax
        
        return max(len(tasks),out)
