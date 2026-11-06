class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp={}
        for s in strs:            
            key=tuple(sorted(s))
            mp.setdefault(key, []).append(s)
        return list(mp.values())
        
