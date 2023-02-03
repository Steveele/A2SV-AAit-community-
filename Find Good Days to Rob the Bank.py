class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:

        decreasing = [1] * len(security)
        count=0
        
        for i in range(1, len(security)):
            if security[i] <= security[i - 1]:
                count += 1
            else:
                count = 0
            decreasing[i] = count
        
        increasing = [0] * len(security)
        increasing[-1] = 1
        count = 0
        for i in range(len(security) - 2 , -1, -1):
            if security[i] <= security[i+1]:
                count += 1
            else:
                count = 0
            increasing[i] = count
        res = []
        
        for i in range(time, len(security) - time):
            if increasing[i] >= time and decreasing[i] >= time:
                res.append(i)
        return res


