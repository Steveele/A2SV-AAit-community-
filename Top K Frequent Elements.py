class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[]for i in range(len(nums)+1)]
        answer=[]

        for n in nums:
            count[n]=1+count.get(n,0)
        for n , c in count.items():
             freq[c].append(n)
        for i in range(len(freq)-1,0,-1):
             for j in freq[i]:
                answer.append(j)
                if(len(answer)==k):
                    return answer

      


