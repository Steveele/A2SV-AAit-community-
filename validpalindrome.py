class Solution:
    def isPalindrome(self, s: str) -> bool:
        out=[]

        for i in s:
            if i.isalnum():
                out.append(i.lower())
        right=len(out)-1
        i=0
        print(out)
        
        while(i<right):
            if out[i]!=out[right]:
                return False
            right-=1
            i+=1
        return True
