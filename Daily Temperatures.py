class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        answer=[0]*len(temperatures)

        for i ,tem in enumerate(temperatures):
            while stack and tem>stack[-1][0]:
                stackvalue,stackindex=stack.pop()
                answer[stackindex]=(i-stackindex)
            stack.append([tem,i])
        return answer
