class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     seen=set()
     left=0
     maxnum=0
     for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1        
        seen.add(s[right])
        maxnum=max(maxnum,right-left+1)
     return maxnum