class Solution:
    def minWindow(self, s: str, t: str) -> str:
     need={}
     for c in t:
        need[c]=need.get(c,0)+1
     bestlen=float("inf")
     bestleft=0
     left=0
     window={}
     have=0
     req=len(need)
     for right in range(len(s)):
        c=s[right]
        window[c]=window.get(c,0)+1
        if c in need and window[c]==need[c]:
            have+=1
        while have == req:
            if right-left+1<bestlen:
                bestlen=right-left+1
                bestleft=left
            window[s[left]]-=1
            c=s[left]
            if c in need and window[c]<need[c]:
                have-=1
            left+=1
     if bestlen==float("inf"):
        return ""
     return s[bestleft:bestleft+bestlen]