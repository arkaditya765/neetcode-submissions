class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         seen={}
         for i,val in enumerate(nums):
          j= target-val
          if j in seen:
            return [seen[j], i]
          else:
            seen[val] = i