from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Freq map is a list of counts
        res = defaultdict(list)

        for s in strs:
            # Create list of counts for a -> z
            count = [0] * 26

            for c in s:
                # Use ascii to add to count
                count[ord(c) - ord("a")] += 1

            # Use the count list as key, append word to list of values
            res[tuple(count)].append(s)
        # Return the values as a list of lists
        return list(res.values())
