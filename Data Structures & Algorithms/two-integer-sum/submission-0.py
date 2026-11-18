class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i,n in enumerate(nums):
            req = target - n
            if req in m:
                return [m.get(req,0),i]
            m[n] = i
        return [-1,-1]
        