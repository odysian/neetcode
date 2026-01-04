class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Length validation
        if len(s) != len(t):
            return False
        # Create freq maps
        f1, f2 = {}, {}

        # Add to both freq maps
        for i in range(len(s)):
            f1[s[i]] = f1.get(s[i], 0) + 1
            f2[t[i]] = f2.get(t[i], 0) + 1

        # Loop through one map, check values match
        for i in f1:
            if f1[i] != f2.get(i, 0):
                return False
        return True
