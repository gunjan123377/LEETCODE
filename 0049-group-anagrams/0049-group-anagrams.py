class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_grp = {}

        for data in strs:
            sorted_data = "".join(sorted(data))
            if sorted_data in anagram_grp:
                anagram_grp[sorted_data].append(data)
            else:
                anagram_grp[sorted_data] = [data]
        return list(anagram_grp.values())



        