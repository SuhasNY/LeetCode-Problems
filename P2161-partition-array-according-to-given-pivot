class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        greater = []
        equal = []
        for i in nums:
            if i < pivot:
                lesser.append(i)

            if i > pivot:
                greater.append(i)

            if i == pivot:
                equal.append(i)
        result = lesser + equal + greater
        return result
    