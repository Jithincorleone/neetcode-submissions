class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hash_map_s={}
        hash_map_t={}

        for val in s:
            if val in hash_map_s.keys():
                hash_map_s[val]=hash_map_s[val]+1
            else:
                hash_map_s[val]=1
        
        for val in t:
            if val in hash_map_t.keys():
                hash_map_t[val]=hash_map_t[val]+1
            else:
                hash_map_t[val]=1
        
        for key,val in hash_map_s.items():
            if key not in hash_map_t.keys():
                return False
            else:
                if hash_map_t[key] !=val:
                    return False

        
        return True




