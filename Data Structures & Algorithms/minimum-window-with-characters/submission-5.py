class Solution:
    def minWindow(self, s: str, t: str) -> str:
     need={}
     window={}
     for c in t:
        need[c]=need.get(c,0)+1
     left=0
     bestleft=0
     bestlen=float("inf")
     required=len(need)
     have=0
     for right in range(len(s)):
        k=s[right]
        window[k]=window.get(k,0)+1
        if k in need and window[k]==need[k]:
            have+=1
        while have==required:
            if right-left+1<bestlen:
                bestlen=right-left+1
                bestleft=left
            k=s[left]
            window[k]-=1
            if k in need and window[k]<need[k]:
                have-=1
            left+=1
     if bestlen==float("inf"):
         return ""
     return s[bestleft:bestleft+bestlen]


