from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams_brute_force(self, strs: List[str]) -> List[List[str]]:
        """
        Brute Force Approach
        Time Complexity: O(N^2 * L log L)
        Space Complexity: O(N * L)
        """
        if len(strs) == 1:
            return [strs]
        res = []
        seen = [False] * len(strs)
        for i in range(len(strs)):
            if seen[i]:
                continue
            seen[i] = True
            part = [strs[i]]
            key = sorted(strs[i])
            for j in range(i + 1, len(strs)):
                if key == sorted(strs[j]) and not seen[j]:
                    part.append(strs[j])
                    seen[j] = True
            res.append(part)
        return res

    def groupAnagrams_sorting(self, strs: List[str]) -> List[List[str]]:
        """
        Optimal (Sorting Signature)
        Time Complexity: O(N * L log L)
        Space Complexity: O(N * L)
        """
        if len(strs) == 1:
            return [strs]
        
        mapping_dict = dict()
        for v in strs:
            key = "".join(sorted(v))
            if key not in mapping_dict:
                mapping_dict[key] = [v]
            else:
                mapping_dict[key].append(v)
        
        return list(mapping_dict.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Optimal (Character Count Signature)
        Time Complexity: O(N * L)
        Space Complexity: O(N * L)
        """
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())
