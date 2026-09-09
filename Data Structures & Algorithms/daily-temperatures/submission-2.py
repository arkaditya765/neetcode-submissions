class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
     stack=[]
     result=[0]*len(temperatures)
     for i,t in enumerate(temperatures):
        while stack and temperatures[stack[-1]]<t:
            prev=stack.pop()
            result[prev]=i-prev
        stack.append(i)
     return result