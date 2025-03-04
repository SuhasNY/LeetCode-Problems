import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        k = 0
        n1 = len(nums1)
        n2 = len(nums2)
        merged = []

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < n1:
            merged.append(nums1[i])
            i += 1

    
        while j < n2:
            merged.append(nums2[j])
            j += 1
    
        if (n1 + n2) % 2 != 0:
            return merged[(n1 + n2)//2]
        else:
            median = (n1 + n2)//2
            return (merged [median] + merged [median - 1]) / 2