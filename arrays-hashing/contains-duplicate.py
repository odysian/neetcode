from collections import defaultdict
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create freq map
        freq = defaultdict(int)
        for n in nums:
            # If value already exists, return True
            if freq[n] > 0:
                return True
            # Add it if doesn't
            freq[n] += 1
        # Return False otherwise
        return False
