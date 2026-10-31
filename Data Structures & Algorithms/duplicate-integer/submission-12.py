class Solution:
        
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash_map={}
        for val in nums:
            if val in hash_map:
                hash_map[val]+=1
            else:
                hash_map[val]=1


        for key,val in hash_map.items():

            if val > 1:
                return True
        
        return False