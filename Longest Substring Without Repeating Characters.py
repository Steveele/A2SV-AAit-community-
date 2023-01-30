class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       sSet=set()
       left=0
       answer=0

       for i in range(len(s)):
           while s[i] in sSet:
               sSet.remove(s[left])
               left+=1
           sSet.add(s[i])
           answer=max(answer,i-left+1)
       return answer
