 piles.sort()
        sum=0
        l,rr,r=0 ,len(piles)-2,len(piles)-1
        while(l<rr):
            sum+=piles[rr]
            rr-=2
            r-=2
            l+=1
        return sum