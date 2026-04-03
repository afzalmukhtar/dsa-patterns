from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams_brute_force(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        res = []
        seen = set()
        for i in range(len(strs)):
            if i in seen:
                continue
            seen.add(i)
            part = [strs[i]]
            key = sorted(strs[i])
            for j in range(i + 1, len(strs)):
                if key == sorted(strs[j]) and j not in seen:
                    part.append(strs[j])
                    seen.add(j)
            res.append(part)
        return res

    def groupAnagrams_sorting(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            groups[sorted_s].append(s)
        return list(groups.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())

sol = Solution()
strs = ["", ""]
print(f"Brute Force: {sol.groupAnagrams_brute_force(strs)}")
print(f"Sorting:     {sol.groupAnagrams_sorting(strs)}")
print(f"Optimal:     {sol.groupAnagrams(strs)}")
