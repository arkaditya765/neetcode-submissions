class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest = 0

        for i in nums:
            if i - 1 not in seen:
             current = i
             length = 1
             while current+1 in seen:
                current+=1
                length+=1
             longest=max(longest,length)
        return longest

          
