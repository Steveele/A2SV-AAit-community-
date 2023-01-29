class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        left = 0
        right = len(cardPoints) - k
        total = sum(cardPoints[right:])
        
        ans = total
        while k>0:
            total += cardPoints[left] - cardPoints[right]
            ans = max(ans, total)
            left += 1
            right += 1
            k-=1
        return ans