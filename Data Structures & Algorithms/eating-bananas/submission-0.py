class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l <= r:
            k = (l + r) // 2
            hour=0
            for pile in piles:
              hour += (pile + k - 1) // k
            if hour<=h:
                r=k-1
            else:
                l=k+1
        return l
