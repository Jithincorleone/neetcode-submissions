from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped=defaultdict(list)

        for val in strs:
            key_s= "".join(sorted(val))
            grouped[key_s].append(val)

        d={key:value for key, value in grouped.items()}
        
        return list(d.values())


            



        

