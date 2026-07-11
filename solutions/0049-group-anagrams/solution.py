class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for current_name in strs:
            nametag = "".join(sorted(current_name))
            seen[nametag].append(current_name)
        return list(seen.values())
