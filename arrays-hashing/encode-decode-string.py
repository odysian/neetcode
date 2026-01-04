from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Encode with length and # delimeter
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # Loop through str, find delim idx
        while i < len(s):
            delim = s.index("#", i)
            # Read numbers preceding delimeter
            length = int(s[i:delim])

            start = delim + 1
            # Append from after delim to length of code
            res.append(s[start : start + length])
            # Set i to after decoded word
            i = start + length
        return res
