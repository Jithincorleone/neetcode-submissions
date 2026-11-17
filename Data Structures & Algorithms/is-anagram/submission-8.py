#from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_s, hash_t={}, {}

        for idx in range(len(s)):

            if s[idx] in hash_s:
                hash_s[s[idx]]+=1
            else:
                hash_s[s[idx]]=1
            
            if t[idx] in hash_t:
                hash_t[t[idx]]+=1
            else:
                hash_t[t[idx]]=1
        
        return hash_t==hash_s

        
        # cntr_s=Counter(s)
        # cntr_t=Counter(t)

        # print(cntr_s)
        # print(cntr_t)

        # return cntr_s==cntr_t
