class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        r_, arr, length = 0, [], len(popped)
        for i in pushed:
            arr.append(i)
            while arr and arr[-1] == popped[r_]:
                arr.pop()
                r_ += 1
        return True if r_ == length else False