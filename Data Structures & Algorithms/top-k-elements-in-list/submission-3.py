class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
          count[num]=count.get(num,0)+1
        buckets = [[] for _ in range(len(nums) + 1)]
        for n,f in count.items():
          buckets[f].append(n)
        result=[]
        for f in range(len(buckets)-1,0,-1):
          for num in buckets[f]:
            result.append(num)
            if len(result)==k:
              return result