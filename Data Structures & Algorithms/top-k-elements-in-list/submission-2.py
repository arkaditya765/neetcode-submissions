class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count={}
      for i in nums:
        count[i]=count.get(i,0)+1
      result=list(count.items())
      result.sort(key=lambda x: x[1],reverse=True)
      ans=[]
      for key,value in result[:k]:
        ans.append(key)

      return ans
      

        