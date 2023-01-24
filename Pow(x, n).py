class Solution:
    def myPow(self, x: float, n: int) -> float:
      if n<0:
          return (1/x)*self.myPow(1/x,-n-1)
      if n==0:
            return 1
      if n==2 :
            return x*x
      if n%2==0:
            return self.myPow(self.myPow(x,n//2),2)
      else:
          return x*self.myPow(self.myPow(x,n//2),2)