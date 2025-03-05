class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, n = 0, len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                res.append(nums[i])
        nums[:] = res
        return len(res)