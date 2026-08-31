class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Sort by frequency (highest first)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans