class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1

        # Store product of elements to the left
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Multiply by product of elements to the right
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output