def binarySearch(array, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def findPivot(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:  
            low = mid + 1
        else:
            high = mid
    return low

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        pivot = findPivot(nums)
        n = len(nums)

        if nums[pivot] <= target <= nums[n-1]:
            return binarySearch(nums, pivot, n-1, target)
        else:
            return binarySearch(nums, 0, pivot-1, target)
