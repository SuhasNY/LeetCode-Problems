class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closestSum = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if abs(threeSum - target) < abs(closestSum - target):
                    closestSum = threeSum
                
                if threeSum == target:
                    return threeSum
                elif threeSum < target:
                    l += 1
                else:
                    r -= 1
        return closestSum