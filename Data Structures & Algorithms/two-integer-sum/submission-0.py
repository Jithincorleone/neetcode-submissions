class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=i
        
        for j in range(len(nums)):
            diff=target-nums[j]
            if diff in hash_map.keys() and hash_map[diff]!=j:
                return [j, hash_map[diff]]
                


