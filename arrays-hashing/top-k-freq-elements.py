from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        # Sort freq map with values as sort key
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # Return list of k values
        return [num for num, count in sorted_items[:k]]
