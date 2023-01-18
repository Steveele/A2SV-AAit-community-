class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split()
        word = {}
        ans =''
        for i in temp:
             word[i[-1]]= i[:-1]

        for key,value in sorted(word.items()):
            ans+=''.join(value)+' '
        ans=ans[:-1]
        return ans
