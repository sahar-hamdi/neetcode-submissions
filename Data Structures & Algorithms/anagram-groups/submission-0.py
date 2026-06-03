from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))

            map_[sorted_word].append(word)

        return list(map_.values())