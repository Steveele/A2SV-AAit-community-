class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        
        for posi , spe in sorted(zip(position,speed))[::-1]:
            time=(target-posi)/spe
            if not stack:
                stack.append(time)
            elif (time>stack[-1]):
                stack.append(time)
        return len(stack)
