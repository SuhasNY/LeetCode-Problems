class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            if len(result) != 0:
                break
            for j in range(0, len(nums)):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break
            
        return result