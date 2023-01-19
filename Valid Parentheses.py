class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close_o={"}":"{","]":"[",")":"("}
        for i in s:
            if i in close_o:
                if stack and stack[-1]==close_o[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

