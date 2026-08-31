
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        
        for num in nums: # Iterating over the set also avoids duplicate work
            # Crucial Fix: Only start building if 'num' is the START of a sequence
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                longest = max(longest, length)
                
        return longest