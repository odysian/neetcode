from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Freq map
        seen = {}
        # Enumerate, calc the value we need to reach target sum
        for i, n in enumerate(nums):
            diff = target - n
            # If we have it in our map, return [diff_idx, idx]
            if diff in seen:
                return [seen[diff], i]
            # Else: store value, idx
            seen[n] = i
        return []
