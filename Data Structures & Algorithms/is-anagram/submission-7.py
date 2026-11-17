from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        cntr_s=Counter(s)
        cntr_t=Counter(t)

        print(cntr_s)
        print(cntr_t)

        return cntr_s==cntr_t
