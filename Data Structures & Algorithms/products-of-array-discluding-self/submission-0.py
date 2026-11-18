class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-2,-1,-1):
            result[i+1] *= right
            right *= nums[i+1]
        result[0]*=right
        return result